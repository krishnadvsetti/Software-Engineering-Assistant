from pathlib import Path


class RepositoryScanner:

    @staticmethod
    def scan(project_path: str) -> dict:

        path = Path(project_path)

        files = []

        for file in path.rglob("*"):

            if file.is_file():
                files.append(file.name)

        return {
            "total_files": len(files),
            "files": files,
        }