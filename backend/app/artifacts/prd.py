from app.artifacts.base import Artifact


class PRDArtifact(Artifact):

    def __init__(
        self,
        title: str,
        summary: str,
    ):

        super().__init__("Product Requirements")

        self.title = title
        self.summary = summary