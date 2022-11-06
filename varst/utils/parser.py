from argparse import ArgumentParser
from typing import Any
from typing import Optional
from typing import Sequence


class Parser:

    _parser = ArgumentParser()

    def __init__(self) -> None:
        self._parser.add_argument(
            "variables", nargs="*",
            help="key-value pairs of substitutions",
        )
        self._parser.add_argument(
            "-i",
            "--input",
            type=str,
            help="rst file path as input",
        )
        self._parser.add_argument(
            "-o",
            "--output",
            type=str,
            help="rst file path as output",
        )

    def parse_args_dict(self, argv: Optional[Sequence[str]]) -> dict[str, Any]:
        args = self._parser.parse_args(argv)
        return vars(args)
