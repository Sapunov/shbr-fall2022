import functools
import pathlib
import typing as tp


class SecretsReader:
    secrets_dir: pathlib.Path

    def __init__(self, secrets_dir: pathlib.Path):
        self.secrets_dir = secrets_dir

    @functools.cache
    def get(self, name: str) -> tp.Optional[str]:
        filename = self.secrets_dir / name.lower()
        if not filename.exists():
            return None
        return filename.read_text().strip()
