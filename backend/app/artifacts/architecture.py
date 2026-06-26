from app.artifacts.base import Artifact


class ArchitectureArtifact(Artifact):

    def __init__(
        self,
        architecture_style: str,
        backend: str,
        frontend: str,
        database: str,
        cache: str,
        deployment: str,
    ):

        super().__init__("Architecture")

        self.architecture_style = architecture_style
        self.backend = backend
        self.frontend = frontend
        self.database = database
        self.cache = cache
        self.deployment = deployment