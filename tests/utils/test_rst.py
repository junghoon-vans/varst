import os.path
from pathlib import Path

import pytest
from docutils.nodes import document as Document

from varst.utils.rst import RstDocument


@pytest.fixture
def rst_document() -> RstDocument:
    test_data_path = os.path.join(
        Path(__file__).resolve().parent.parent, 'data',
    )
    return RstDocument(src=os.path.join(test_data_path, 'README.rst'))


def test_get_document(rst_document: RstDocument):

    assert isinstance(rst_document.document, Document)


def test_substitution_text(rst_document: RstDocument):
    assert rst_document.substitution_text("status") == "false"


def test_replace_substitution(rst_document: RstDocument):
    rst_document.replace_substitution("status", "true")
    assert rst_document.substitution_text("status") == "true"


def test_save(rst_document: RstDocument, tmp_path):
    rst_document.save(dest=os.path.join(tmp_path, "test.rst"))
