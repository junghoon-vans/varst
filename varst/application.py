"""Module containing the application class"""
from typing import Optional
from typing import Sequence

from varst.utils.parser import Parser


class Application:
    """Application class"""

    def __init__(self) -> None:
        self.parser = Parser()

    def run(self, argv: Optional[Sequence[str]]):
        """Run application

            Args:
                argv: Arguments vector

        """
        args_dict = self.parser.parse_args_dict(argv)
        print(args_dict)
