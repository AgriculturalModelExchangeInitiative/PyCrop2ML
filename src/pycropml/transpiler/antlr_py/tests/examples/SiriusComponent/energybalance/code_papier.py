import xml.etree.ElementTree as xml


def modelcomposition(xfile):
    doc = xml.parse(xfile)
    root = doc.getroot()
    compositeid = root.attrib["class"]
    id = compositeid
    compositeid = compositeid.split(
        ".")[-1] if "." in compositeid else compositeid
    name = compositeid
    mc = ModelComposition({"name": name, "version": "001", "timestep": "1"})
    desc = {}
    desc["name"] = name
    desc["authors"] = "Gunther Krauss"
    desc["institution"] = "INRES Pflanzenbau, Uni Bonn"
    desc["Reference"] = "http://www.simplace.net/doc/simplace_modules/"
    desc["description"] = "as given in the documentation"
    desc["url"] = "http://www.simplace.net/doc/simplace_modules/"
    description = model_desc(desc)
    mc.add_description(description)
    mods = []
    for el in list(root):
        for l in list(el):
            mu_name = l.attrib["id"]
            mods.append(mu_name)
            for j in list(l):
                attr = j.attrib
                if j.tag == "input" and "source" in attr:
                    id = attr["id"]
                    var = attr["source"].split(".")[-1]
                    mod = attr["source"].split(".")[0]
                    if mod == name or mod not in mods:
                        mc.inputlink.append(
                            {"target": mu_name + "." + id, "source": var})
                    elif mod in mods:
                        mc.internallink.append(
                            {"source": mod + "." + var, "target": mu_name + "." + id})
                elif j.tag == "output":
                    id = attr["id"]
                    var = attr["destination"].split(".")[-1]
                    mod = attr["destination"].split(".")[0]
                    mc.outputlink.append(
                        {"source": mu_name + "." + id, "target": var})
    mc.model = mods
    return mc
