import argparse
import re
from argparse import ArgumentParser
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence


class Parser:
    """Parser class that parse arguments from cli"""

    _parser = ArgumentParser()

    input_file: str = ""
    output_file: str = ""
    variables: Dict[str, str] = {}

    def __init__(self) -> None:
        self._parser.add_argument(
            "variables", nargs="*",
            help="key-value pairs of substitutions",
            type=_pattern_type,
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
        """ Parse the arguments from argv.
            Parsed values are updated in the attributes of the parser.

            Args:
                argv: Arguments vector

        """
        args = self._parser.parse_args(argv)
        arg_dict = vars(args)

        self.input_file = arg_dict['input']
        self.output_file = arg_dict['output']
        self.variables = _parse_kv(arg_dict['variables'])


_VARIABLE_PATTERN = re.compile(r"[^=]+=[^=]+")


def _pattern_type(arg_value: str, pat=_VARIABLE_PATTERN):
    """ Verify that the arg_value fully matches the pattern.

        Args:
            arg_value: The string value to check pattern.
            pat: The pattern to match value.
        Returns:
            str: Returns arg_value that matched with pattern.

    """
    if not pat.fullmatch(arg_value):
        raise argparse.ArgumentTypeError(f"invalid pattern: {pat.pattern}")
    return arg_value


def _parse_kv(variables: List[str]) -> Dict[str, str]:
    """Parse ``key-value`` pair from variables.

        Args:
            variables: The string list to be parsed.
        Returns:
            Dict[str, str]: key-value pair

    """
    result: Dict[str, str] = {}

    for variable in variables:
        kv = variable.split("=")
        result[kv.pop()] = kv.pop()

    return result
