Architecture des plateformes de transformation
===============================================

Objectif de la refactorisation
------------------------------

PyCropML réalise deux familles de transformations :

* une **plateforme source** transforme un composant provenant d'un framework
  (APSIM, BioMA, Python, etc.) en package Crop2ML ;
* une **plateforme cible** transforme un package Crop2ML en code ou en package
  utilisable par un langage ou un framework cible (Python, OpenAlea, Java,
  C#, etc.).

Historiquement, ``cyml.py`` connaissait directement les modules, les classes,
les chemins et les particularités de chaque plateforme. Cette organisation
créait un couplage fort : ajouter une plateforme pouvait imposer de modifier
plusieurs endroits du coeur de PyCropML.

La nouvelle architecture sépare les responsabilités au moyen de contrats de
plateformes, de registres, d'une façade, d'un pipeline et d'un contexte de
génération.

Vue d'ensemble
--------------

Le flux d'une transformation vers une cible est le suivant::

    Utilisateur ou CLI
           |
           v
    cyml.transpile_package()          façade publique
           |
           v
    TargetPipeline                    orchestration
           |
           +----> target_registry ----> TargetPlatform
           |
           +----> GenerationContext
           |
           +----> générateur de ModelUnit
           +----> générateur de composition
           +----> hooks optionnels

Le flux d'une transformation depuis une plateforme source est plus direct::

    cyml.transpile_component()
           |
           v
    source_registry ----> SourcePlatform.convert()
                              |
                              v
                         package Crop2ML

Programmation par contrat
-------------------------

La **programmation par contrat** consiste à définir explicitement ce qu'un
composant doit fournir et ce que le reste du système peut attendre de lui. Le
code appelant dépend du contrat et non de l'implémentation concrète.

Dans cette architecture, les contrats publics sont principalement :

``SourcePlatform``
    Décrit une plateforme d'entrée et expose l'opération ``convert``. Le
    contrat garantit qu'une source enregistrée sait convertir un composant
    externe vers Crop2ML.

``TargetPlatform``
    Décrit une cible : nom, module Python, générateur de ModelUnit, compositeur,
    extension de fichier et capacités optionnelles. Le pipeline utilise ce
    contrat sans importer directement un générateur Python, OpenAlea ou Java.

``GenerationContext``
    Définit les informations mises à la disposition des étapes de génération :
    modèles, composition, nom du composant, répertoires de travail, métadonnées
    et options.

Il s'agit ici d'une conception **orientée contrat** : les types, champs requis
et méthodes publiques forment le contrat. Ce n'est pas encore une mise en
oeuvre formelle du *Design by Contract* avec des préconditions, postconditions
et invariants vérifiés par un framework spécialisé. Certaines préconditions
sont néanmoins contrôlées, par exemple le refus d'un ``TargetPlatform`` dont
le nom ou le module est vide.

Les contrats apportent les garanties suivantes :

* la CLI peut distinguer une source d'une cible ;
* les plateformes intégrées utilisent toutes la même interface ;
* le coeur ne dépend plus directement de chaque implémentation ;
* les capacités facultatives sont exprimées explicitement ;
* les futures plateformes externes pourront adopter le même contrat.

Le design pattern Façade
------------------------

Une **Façade** fournit une interface simple et stable devant un sous-système
plus complexe. Elle masque l'enchaînement des opérations et réduit le nombre
d'objets que l'appelant doit connaître.

Le module ``pycropml.cyml`` joue ce rôle. Ses fonctions restent les points
d'entrée publics :

* ``transpile_file(source, language)`` ;
* ``transpile_package(package, language)`` ;
* ``transpile_component(component, package, language)``.

Par exemple, l'appelant continue d'écrire::

    from pycropml.cyml import transpile_package

    transpile_package("energybalance_pkg", "py")

Il n'a pas besoin de créer lui-même le registre, la topologie, le contexte ou
le pipeline. Pour la génération d'un package, la façade délègue désormais à::

    TargetPipeline(package, language).run()

Cette délégation permet de faire évoluer l'implémentation interne sans changer
l'API utilisée par la CLI, les notebooks et les applications clientes.

Le registre (*Registry pattern*)
--------------------------------

Un **registre** associe un identifiant stable à une description d'objet ou à
une fabrique. Il évite les suites de ``if/elif`` dispersées et constitue la
source de vérité sur les plateformes disponibles.

``source_registry.py``
    Associe un nom tel que ``apsim`` ou ``bioma`` à un ``SourcePlatform``.

``target_registry.py``
    Associe un nom tel que ``py`` ou ``openalea`` à un ``TargetPlatform``.

La résolution est donc conceptuellement la suivante::

    nom fourni par la CLI
             |
             v
    get_source(nom) ou get_target(nom)
             |
             v
    contrat de plateforme

Les classes et fonctions concrètes sont chargées de manière différée (*lazy
loading*) au moyen de ``importlib``. Une dépendance particulière n'est donc
importée que lorsque la plateforme correspondante en a besoin.

Le pattern Pipeline
-------------------

Un **Pipeline** organise une transformation en étapes ordonnées. Chaque étape
reçoit les résultats ou le contexte préparé par les étapes précédentes.

``TargetPipeline`` porte maintenant l'orchestration autrefois contenue dans
``cyml.transpile_package``. Son ordre d'exécution est :

#. résoudre et valider le ``TargetPlatform`` demandé ;
#. parser les fichiers XML Crop2ML afin d'obtenir les ModelUnits ;
#. créer les répertoires de sortie ;
#. générer les modèles intermédiaires CyML ;
#. construire la topologie de la composition ;
#. compléter le ``GenerationContext`` ;
#. appeler les hooks de classes de domaine et de wrapper ;
#. transformer chaque ModelUnit vers la cible ;
#. générer l'algorithme et le code de la composition ;
#. appeler le hook optionnel de simulation.

L'ordre doit être conservé. Par exemple, la transformation des ModelUnits lit
les fichiers CyML créés précédemment, et la génération des hooks nécessite la
composition obtenue par ``Topology``.

Le pipeline est responsable du **quand** et du **dans quel ordre**. Le
``TargetPlatform`` est responsable du **quoi charger ou appeler**. Les
générateurs concrets restent responsables du **comment produire le code**.

Le contexte de génération
-------------------------

``GenerationContext`` est un **Context Object** : il regroupe les données
nécessaires à plusieurs opérations afin d'éviter des listes d'arguments longues
et différentes pour chaque plugin.

Ses champs représentent :

``package``
    Chemin racine du package Crop2ML traité.

``package_name``
    Nom du package tel qu'il apparaît dans le système de fichiers.

``target_name``
    Identifiant de la cible résolue dans le registre.

``model_units``
    Objets ModelUnit construits à partir des descriptions XML.

``composition``
    Modèle composite produit par ``Topology``.

``component_name``
    Nom de la composition ou du composant principal.

``crop2ml_directory``
    Répertoire contenant les descriptions XML Crop2ML.

``cyml_directory``
    Répertoire des algorithmes intermédiaires CyML/``pyx``.

``target_root``
    Répertoire racine de la cible, par exemple ``src/py``.

``target_package``
    Répertoire du package généré, par exemple
    ``src/py/energybalance_pkg``.

``test_directory``
    Répertoire des tests propres à la cible.

``documentation_directory`` et ``image_directory``
    Répertoires destinés à la documentation et aux graphes produits.

``metadata``
    Dictionnaire extensible pour des informations descriptives additionnelles.

``options``
    Dictionnaire extensible pour les options d'une exécution donnée.

Les deux dictionnaires rendent possibles de petites extensions sans modifier
immédiatement le constructeur du contexte. Une donnée fondamentale et commune
à toutes les plateformes doit toutefois devenir un champ explicite plutôt
qu'une clé implicite dans ``options``.

Les hooks
---------

Un **hook** est un point d'extension appelé par le coeur lorsqu'une plateforme
déclare la capacité correspondante. Il permet d'ajouter un comportement sans
insérer une condition spécifique dans le pipeline.

Les hooks cibles actuels sont :

``domain_class_factory``
    Produit les classes de domaine requises par certaines plateformes.

``wrapper_factory``
    Produit un adaptateur ou wrapper autour de la composition.

``simulation_class``
    Produit les fichiers permettant d'exécuter une simulation. Cette capacité
    est actuellement utilisée par la cible Python.

``generate_notebooks``
    Indique que des notebooks de test doivent être produits pour les
    ModelUnits.

Un hook absent est une capacité non supportée et non une erreur. Le pipeline
continue simplement sans exécuter cette étape optionnelle.

Compatibilité avec les générateurs historiques
----------------------------------------------

Les anciens hooks n'acceptaient pas encore directement un
``GenerationContext``. ``TargetPlatform`` joue temporairement le rôle
d'**adaptateur** entre le nouveau pipeline et ces signatures historiques.

Par exemple, le pipeline appelle conceptuellement::

    target.generate_wrapper(context)

et ``TargetPlatform`` transforme cet appel vers la signature existante::

    wrapper_factory(
        context.composition,
        context.target_package,
        context.component_name,
    )

Ce mécanisme correspond au **Adapter pattern** : une interface nouvelle est
convertie vers une interface existante sans réécrire immédiatement tous les
générateurs. À terme, les nouveaux hooks pourront consommer directement le
contexte, après définition d'une politique de compatibilité et de versionnage.

Répartition des responsabilités
-------------------------------

=============================== =============================================
Élément                         Responsabilité
=============================== =============================================
``cyml.py``                     Façade publique appelée par la CLI et le code
                                utilisateur.
``SourcePlatform``              Contrat d'une conversion vers Crop2ML.
``TargetPlatform``              Contrat et capacités d'une cible.
``source_registry.py``          Catalogue et résolution des sources.
``target_registry.py``          Catalogue et résolution des cibles.
``TargetPipeline``              Orchestration ordonnée d'une génération cible.
``GenerationContext``           Données partagées par les étapes et les hooks.
``Main``                        Parsing/transformation d'un algorithme de
                                ModelUnit vers le langage cible.
``Topology``                    Lecture et traduction de la composition.
Générateurs concrets            Production du code propre à une plateforme.
=============================== =============================================

Ajouter une plateforme intégrée
--------------------------------

Dans l'architecture actuelle, une plateforme intégrée à PyCropML suit les
étapes suivantes :

#. implémenter son convertisseur source ou ses générateurs cibles dans un
   module dédié ;
#. déclarer un ``SourcePlatform`` ou un ``TargetPlatform`` dans le registre
   correspondant ;
#. déclarer uniquement les capacités optionnelles réellement supportées ;
#. ajouter des tests vérifiant le chargement différé et le respect du contrat ;
#. ajouter au moins un test de transformation représentatif.

Exemple conceptuel d'une cible::

    TargetPlatform(
        name="ma_plateforme",
        module="pycropml.transpiler.generators.ma_plateforme",
        generator="ModelUnitGenerator",
        composer="CompositionGenerator",
        extension="py",
        wrapper_factory="generate_wrapper",
        generate_notebooks=True,
    )

Le pipeline n'a pas à être modifié si la plateforme se limite aux capacités du
contrat. Une nouvelle capacité transversale doit d'abord être définie dans le
contrat, documentée, puis orchestrée par le pipeline.

Limite actuelle et extension externe
------------------------------------

Les plateformes intégrées sont encore déclarées dans les registres du dépôt
PyCropML. Les contrats, la façade et le contexte constituent la préparation
nécessaire à des packages externes, mais leur découverte automatique n'est pas
encore implémentée.

L'étape suivante pourra utiliser les **entry points Python**. Un package tiers
déclarera alors sa plateforme dans son ``pyproject.toml`` ; PyCropML la
découvrira à l'exécution sans modification de son registre interne. Cette
évolution devra préserver les mêmes contrats et fournir une erreur claire en
cas de plugin incompatible.

Principes de maintenance
------------------------

Pour conserver cette séparation :

* ne pas importer un générateur de plateforme directement dans ``cyml.py`` ;
* ne pas ajouter de condition ``if target == ...`` dans le pipeline lorsque le
  comportement peut être représenté par une capacité ou un hook ;
* faire transiter les informations de génération par ``GenerationContext`` ;
* maintenir ``transpile_package`` comme API stable ;
* charger les dépendances optionnelles uniquement lors de l'utilisation de la
  plateforme concernée ;
* tester séparément le contrat, l'orchestration et une génération réelle.
