from app.artifacts.base import Artifact


class RepositoryAnalysisArtifact(Artifact):

    def __init__(
        self,
        language: str,
        framework: str,
        database: str,
        package_manager: str,
        containers: bool,
        ci_cd: str,
    ):

        super().__init__("Repository Analysis")

        self.language = language
        self.framework = framework
        self.database = database
        self.package_manager = package_manager
        self.containers = containers
        self.ci_cd = ci_cd