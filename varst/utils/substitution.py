import re
from typing import Match
from typing import Optional

from varst.utils.rst_file import RstFile


class Substitution:

    def __init__(self, rst_file: RstFile):
        self.rst_file = rst_file

    def find(self, text: str) -> str:
        """Find substitution definition by substitution text.

        Args:
            text: The string value of substitution text.
        Returns:
            Returns substitution definition if it exists.
        Raises:
            KeyError: If substitution definition is not in file.

        """
        pattern = fr"""\.\.[ ]+\|({text})\|"""

        for content in self.rst_file.contents:
            if re.match(pattern, content):
                return content
        raise KeyError(text)

    def update(self, text: str, data: str) -> None:
        """Update substitution definition by using substitution text and data.

        Args:
            text: The string value of substitution text.
            data: The string value of substitution data.

        """
        origin = self.find(text)
        new = substitution_def(text, data, directive_type(origin))

        origin_idx = self.rst_file.contents.index(origin)
        self.rst_file.contents.pop(origin_idx)
        self.rst_file.contents.insert(origin_idx, new + "\n")


def substitution_def(
    text: str, data: str,
    directive: str = 'replace',
) -> str:
    """Create substitution definition by using substitution text and data.

    Args:
        text: The string value of substitution text.
        data: The string value of substitution data.
        directive: The string value of directive type.
    Returns:
        Returns substitution definition.

    """
    return f'.. |{text}| {directive}:: {data}'


def directive_type(substitution: str) -> str:
    """Get directive type from substitution definition.

    Args:
        substitution: The string value of substitution definition.
    Returns:
        Returns directive type.
    Raises:
        ValueError: If directive type is not valid.

    """

    pattern = r"""\|(.*)\|(.*?)::"""
    result: Optional[Match[str]] = re.search(pattern, substitution)
    if result:
        return result.group(2).strip()
    raise ValueError("directive type is not valid")
