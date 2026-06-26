from abc import ABC
from datetime import datetime


class Artifact(ABC):

    def __init__(
        self,
        artifact_type: str,
    ):

        self.artifact_type = artifact_type
        self.created_at = datetime.utcnow()

    def to_dict(self):

        return self.__dict__