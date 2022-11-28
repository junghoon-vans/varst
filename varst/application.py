"""Module containing the application class"""
from typing import Optional
from typing import Sequence

from varst.utils.parser import Parser
from varst.utils.rst_file import RstFile
from varst.utils.substitution import Substitution


class Application:
    """Application class"""

    def __init__(self) -> None:
        self.parser = Parser()

    def run(self, argv: Optional[Sequence[str]]) -> None:
        """Run application to replace substitutions.

            Args:
                argv: Arguments vector

        """
        self.parser.parse(argv)

        rst_file = RstFile(src=self.parser.input_file)
        substitution = Substitution(rst_file)
        for k, v in self.parser.sub_pairs.items():
            substitution.update(k, v)
        rst_file.save(dest=self.parser.output_file)
