import pytest

from varst.utils.parser import Parser


@pytest.fixture
def parser() -> Parser:
    parser = Parser()
    return parser


def test_parse_args(parser: Parser):

    assert parser.parse_args_dict(['varst=variable to reStructuredText']) == {
        'variables': ['varst=variable to reStructuredText'],
        'input': './README.rst',
        'output': './README.rst',
    }

    assert parser.parse_args_dict(
        [
            'varst=variable to reStructuredText',
            '-i=./CHANGELOG.rst', '-o=./CHANGELOG.rst',
        ],
    ) == {
        'variables': ['varst=variable to reStructuredText'],
        'input': './CHANGELOG.rst',
        'output': './CHANGELOG.rst',
    }
