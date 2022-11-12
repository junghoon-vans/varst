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
