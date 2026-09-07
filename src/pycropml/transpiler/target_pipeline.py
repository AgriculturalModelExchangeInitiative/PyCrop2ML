"""Orchestration of Crop2ML package generation for a target platform."""

from pathlib import Path

from pycropml import nameconvention, render_cyml
from pycropml.code2nbk import Model2Nb
from pycropml.pparse import model_parser
from pycropml.topology import Topology
from pycropml.transpiler.generation_context import GenerationContext
from pycropml.transpiler.main import Main
from pycropml.transpiler.target_registry import get_target


def _model_prefix(model):
    return model.modelid.split(".")[0]


class TargetPipeline:
    """Generate one target package while keeping ``cyml`` as a facade."""

    def __init__(self, package, target_name):
        self.package = Path(package)
        self.target_name = target_name
        self.target = get_target(target_name)
        if self.target.extension is None:
            raise ValueError(
                f"Target {target_name!r} does not define a file extension"
            )

    def run(self):
        """Run all package-generation stages and return a process status."""
        models = model_parser(self.package)
        context = self._prepare_context(models)

        package_renderer = render_cyml.Model2Package(
            models,
            dir=context.package / "src",
        )
        package_renderer.generate_package()
        package_renderer.write_tests()

        topology = Topology(context.package_name, context.package)
        context.composition = topology.model
        context.component_name = topology.model.name

        self.target.generate_domain_classes(context)
        self.target.generate_wrapper(context)
        self._generate_model_units(context)
        self._generate_composition(context, topology)
        self.target.generate_simulation(context)
        return 0

    def _prepare_context(self, models):
        output = self.package / "src"
        test_directory = self.package / "test"
        documentation_directory = self.package / "doc"
        image_directory = documentation_directory / "images"
        target_root = output / self.target_name
        target_package = target_root / self.package.name.replace("-", "_")
        target_test_directory = test_directory / self.target_name

        for directory in (
            output,
            test_directory,
            documentation_directory,
            image_directory,
            target_root,
            target_package,
            target_test_directory,
        ):
            directory.mkdir(exist_ok=True)

        return GenerationContext(
            package=self.package,
            package_name=self.package.name,
            target_name=self.target_name,
            model_units=models,
            composition=None,
            component_name="",
            crop2ml_directory=self.package / "crop2ml",
            cyml_directory=output / "pyx",
            target_root=target_root,
            target_package=target_package,
            test_directory=target_test_directory,
            documentation_directory=documentation_directory,
            image_directory=image_directory,
        )

    def _generate_model_units(self, context):
        for source_file in (
            path for path in context.cyml_directory.iterdir() if path.is_file()
        ):
            source = source_file.read_text(encoding="utf-8")
            name = source_file.stem
            for model in context.model_units:
                if (
                    name.lower() == model.name.lower()
                    and _model_prefix(model) != "function"
                ):
                    transpiler = Main(
                        source_file,
                        self.target_name,
                        model,
                        context.component_name,
                    )
                    transpiler.parse()
                    transpiler.to_ast(source)
                    code = transpiler.to_source()
                    signature = nameconvention.signature(
                        model,
                        self.target.extension,
                    )
                    destination = (
                        context.target_package
                        / f"{signature}.{self.target.extension}"
                    )
                    destination.write_text(code, encoding="utf-8")
                    if self.target.generate_notebooks:
                        Model2Nb(
                            model,
                            code,
                            name,
                            context.test_directory,
                        ).generate_nb(
                            self.target_name,
                            context.target_package,
                            context.package_name,
                            context.component_name,
                        )

    def _generate_composition(self, context, topology):
        composition_source = topology.algo2cyml(context.image_directory)
        cyml_file = (
            context.cyml_directory
            / f"{context.component_name}Component.pyx"
        )
        cyml_file.write_text(composition_source, encoding="utf-8")

        code = topology.compotranslate(self.target_name)
        if code:
            extension = self.target.effective_composition_extension
            destination = (
                context.target_package
                / f"{context.component_name}Component.{extension}"
            )
            destination.write_text(code, encoding="utf-8")
