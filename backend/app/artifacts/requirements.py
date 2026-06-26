from app.artifacts.base import Artifact


class RequirementsArtifact(Artifact):

    def __init__(
        self,
        functional: list[str],
        non_functional: list[str],
    ):

        super().__init__("Requirements")

        self.functional = functional
        self.non_functional = non_functional