import re

from varst.utils.rst_file import RstFile


class Substitution:

    def __init__(self, rst_file: RstFile):
        self.rst_file = rst_file

    def find(self, name) -> str:
        """Find substitution text by name.

        Args:
            name: The string value of substitution name.
        Returns:
            substitution_text: The string value of substitution text.
        Raises:
            KeyError: If substitution is not in file.

        """
        pattern = re.compile(
            fr"""
                \.\.[ ]+          # explicit markup start
                \|                # substitution indicator
                ({name})\|        # substitution name
            """, re.VERBOSE,
        )

        for content in self.rst_file.contents:
            if pattern.match(content):
                return content
        raise KeyError(name)


def substitution_text(name, value) -> str:
    return f'.. |{name}| replace:: {value}'
