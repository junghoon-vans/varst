from typing import List


class RstFile:
    """Class to handle rst file

    Args:
        src: The source path to open rst file.
    """

    def __init__(self, src: str):
        with open(src, encoding='utf-8') as f:
            self._contents = f.readlines()

    @property
    def contents(self) -> List[str]:
        return self._contents

    def save(self, dest: str) -> None:
        """Save contents to the destination path.

        Args:
            dest: The destination path to save rst file.

        """
        with open(dest, encoding='utf-8', mode='w') as f:
            f.write("".join(self.contents))
