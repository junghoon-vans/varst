import os.path
from pathlib import Path

from docutils.nodes import document as Document

from varst.utils.rst import RstDocument


TEST_DATA_DIR = os.path.join(Path(__file__).resolve().parent.parent, 'data')


def test_get_document():
    rst_document = RstDocument(src=os.path.join(TEST_DATA_DIR, 'README.rst'))
    assert isinstance(rst_document.document, Document)
