import pytest

from varst.utils.parser import Parser


@pytest.fixture
def parser() -> Parser:
    parser = Parser()
    return parser


def test_parse_without_file_path(parser: Parser):
    parser.parse([
        'varst=variable to reStructuredText',
    ])

    assert parser.variables == ['varst=variable to reStructuredText']
    assert parser.input_file == './README.rst'
    assert parser.output_file == './README.rst'


def test_parse_with_file_path(parser: Parser):
    parser.parse([
        '-i=./CHANGELOG.rst', '-o=./CHANGELOG.rst',
    ])

    assert parser.input_file == './CHANGELOG.rst'
    assert parser.output_file == './CHANGELOG.rst'
