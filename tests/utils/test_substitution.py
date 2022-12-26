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
    full_name = substitution.find("RST")
    logo_image = substitution.find("logo")

    print(full_name)
    print(logo_image)

    with pytest.raises(KeyError):
        substitution.find("not exist name")


def test_update_substitution(substitution: Substitution):
    substitution.update("RST", "rst")
    substitution.update("logo", "https://example.com/")

    assert substitution.find("RST") == """.. |RST| replace:: rst\n"""
    assert substitution.find("logo")\
        == """.. |logo| image:: https://example.com/\n"""


def test_create_substitution():
    assert substitution_def("key", "value") == """.. |key| replace:: value"""


def test_directive_type():
    substitution = ".. |badge| image:: https://example.com/"
    assert directive_type(substitution) == "image"
