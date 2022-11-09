import argparse
import re
from argparse import ArgumentParser
from typing import List
from typing import Optional
from typing import Sequence


def _variable_type(arg_value, pat=re.compile(r"[a-zA-Z]+=[a-zA-Z]+")):
    if not pat.match(arg_value):
        raise argparse.ArgumentTypeError("invalid value")
    return arg_value


class Parser:

    _parser = ArgumentParser()

    input_file: str = ""
    output_file: str = ""
    variables: List[str] = []

    def __init__(self) -> None:
        self._parser.add_argument(
            "variables", nargs="*",
            help="key-value pairs of substitutions",
            type=_variable_type,
        )
        self._parser.add_argument(
            "-i",
            "--input",
            type=str,
            help="rst file path as input",
            default="./README.rst",
        )
        self._parser.add_argument(
            "-o",
            "--output",
            type=str,
            help="rst file path as output",
            default="./README.rst",
        )

    def parse(self, argv: Optional[Sequence[str]]) -> None:
        args = self._parser.parse_args(argv)
        arg_dict = vars(args)

        self.input_file = arg_dict['input']
        self.output_file = arg_dict['output']
        self.variables = arg_dict['variables']
