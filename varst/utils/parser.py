import argparse
import os
import re
from argparse import ArgumentParser
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence

from varst import supported


class Parser:
    """Parser class that parse arguments from cli"""

    def __init__(self) -> None:
        self._parser = ArgumentParser()
        self.input_file: str = ""
        self.output_file: str = ""
        self.sub_pairs: Dict[str, str] = {}

        self._parser.add_argument(
            "substitutions", nargs="*",
            help="pairs of substitution definition. format is 'text=data'",
            type=_pattern_type,
        )
        self._parser.add_argument(
            "-i",
            "--input",
            type=_file_type,
            help="rst file path as input",
            default="./README.rst",
        )
        self._parser.add_argument(
            "-o",
            "--output",
            type=_file_type,
            help="rst file path as output",
        )

    def parse(self, argv: Optional[Sequence[str]]) -> None:
        """Parse the arguments from argv.
        Parsed values are updated in the attributes of the parser.

        Args:
            argv: Arguments vector

        """
        args = self._parser.parse_args(argv)
        arg_dict = vars(args)

        self.input_file = self.output_file = arg_dict['input']
        if arg_dict['output'] is not None:
            self.output_file = arg_dict['output']
        self.sub_pairs = _parse_kv(arg_dict['substitutions'])


_VARIABLE_PATTERN = re.compile(r"[^=]+=[^=]+")


def _pattern_type(arg_value: str, pat=_VARIABLE_PATTERN) -> str:
    """Verify that the arg_value fully matches the pattern.

    Args:
        arg_value: The string value to check pattern.
        pat: The pattern to match value.
    Returns:
        Returns arg_value if pattern matched.
    Raises:
        argparse.ArgumentTypeError

    """
    if not pat.fullmatch(arg_value):
        raise argparse.ArgumentTypeError(f"invalid pattern: {pat.pattern}")
    return arg_value


def _file_type(file_name: str) -> str:
    """Verify that the file extension is correct.

    Args:
        file_name: The file name to check file extension.
    Returns:
        Returns file name if file extension is correct.
    Raises:
        argparse.ArgumentTypeError

    """

    ext = os.path.splitext(file_name)[1][1:]
    if ext.lower() not in supported:
        raise argparse.ArgumentTypeError(
            f"file extension must be in {supported}",
        )
    return file_name


def _parse_kv(variables: List[str]) -> Dict[str, str]:
    """Parse ``key-value`` pair from variables.

    Args:
        variables: The string list to be parsed.
    Returns:
        key-value pair

    """
    result: Dict[str, str] = {}

    for variable in variables:
        kv = variable.split("=")
        result[kv.pop()] = kv.pop()

    return result
