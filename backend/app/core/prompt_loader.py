from pathlib import Path


class PromptLoader:

    @staticmethod
    def load(prompt_path: str) -> str:
        return Path(prompt_path).read_text(encoding="utf-8")