import os
from pathlib import Path

import pytest

from varst.utils.rst_file import RstFile
from varst.utils.substitution import directive_type
from varst.utils.substitution import Substitution
from varst.utils.substitution import substitution_def

TEST_DATA_PATH = os.path.join(
    Path(__file__).resolve().parent.parent, 'data',
)


@pytest.fixture
def substitution() -> Substitution:
    rst_file = RstFile(src=os.path.join(TEST_DATA_PATH, 'README.rst'))
    return Substitution(rst_file)


def test_find_substitution(substitution: Substitution):
    none_whitespace = substitution.find("status")
    with_whitespace = substitution.find("with whitespace")

    print(none_whitespace)
    print(with_whitespace)

    with pytest.raises(KeyError):
        substitution.find("not exist name")


def test_update_substitution(substitution: Substitution):
    substitution.update("status", "true")
    substitution.update("with whitespace", "true")
    substitution.update("badge", "success")

    assert substitution.find("status") == """.. |status| replace:: true\n"""
    assert substitution.find(
        "with whitespace",
    ) == """.. |with whitespace| replace:: true\n"""
    assert substitution.find("badge") == """.. |badge| image:: success\n"""


def test_create_substitution():
    assert substitution_def("key", "value") == """.. |key| replace:: value"""


def test_directive_type():
    substitution = ".. |badge| image:: https://example.com/"
    assert directive_type(substitution) == "image"
