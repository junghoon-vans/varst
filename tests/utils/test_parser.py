from typing import Generator

import pytest

from tests.utils import argparse_error
from varst.utils.parser import Parser


@pytest.fixture(scope="session")
def parser() -> Generator[Parser, None, None]:
    parser = Parser()
    parser.parse([
        'varst=variable to reStructuredText',
        'version=0.2.0',
        'release=v0.2.0',
        'url=https://example.com?query=new-value',
    ])
    yield parser


def test_parse_sub_pairs(parser: Parser):
    assert parser.sub_pairs == {
        'varst': 'variable to reStructuredText',
        'version': '0.2.0',
        'release': 'v0.2.0',
        'url': 'https://example.com?query=new-value',
    }


def test_parse_without_file_path(parser: Parser):
    assert parser.input_file == './README.rst'
    assert parser.output_file == './README.rst'


def test_parse_without_substitutions(parser: Parser):
    with pytest.raises(ValueError):
        parser.parse(['-i=./CHANGELOG.rst', '-o=./CHANGELOG.rst'])


def test_parse_with_file_path(parser: Parser):
    parser.parse([
        'varst=variable to reStructuredText',
        '-i=./CHANGELOG.rst', '-o=./CHANGELOG.rst',
    ])

    assert parser.input_file == './CHANGELOG.rst'
    assert parser.output_file == './CHANGELOG.rst'


def test_parse_one_element(parser: Parser):
    with argparse_error():
        parser.parse(['one'])
    with argparse_error():
        parser.parse(['key='])
    with argparse_error():
        parser.parse(['=value'])
