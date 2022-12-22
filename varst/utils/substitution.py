import re

from varst.utils.rst_file import RstFile


class Substitution:

    def __init__(self, rst_file: RstFile):
        self.rst_file = rst_file

    def find(self, name: str) -> str:
        """Find substitution definition by name.

        Args:
            name: The string value of substitution name.
        Returns:
            Returns substitution definition if it exists.
        Raises:
            KeyError: If substitution definition is not in file.

        """
        pattern = fr"""\.\.[ ]+\|({name})\|"""

        for content in self.rst_file.contents:
            if re.match(pattern, content):
                return content
        raise KeyError(name)

    def update(self, name: str, value: str) -> None:
        """Update substitution definition with name to value.

        Args:
            name: The string value of substitution name.
            value: The string value of substitution text.

        """
        origin = self.find(name)
        new = substitution_def(name, value)

        origin_idx = self.rst_file.contents.index(origin)
        self.rst_file.contents.pop(origin_idx)
        self.rst_file.contents.insert(origin_idx, new + "\n")


def substitution_def(name: str, value: str) -> str:
    """Create substitution definition by using name and value.

    Args:
        name: The string value of substitution name.
        value: The string value of substitution text.
    Returns:
        Returns substitution definition.

    """
    return f'.. |{name}| replace:: {value}'
