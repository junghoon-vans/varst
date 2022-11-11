import docutils
from docutils.core import Publisher
from docutils.nodes import document as Document
from docutils.parsers.rst import Parser
from docutils.utils import new_document


class RstDocument:

    def __init__(self, src: str):
        settings = Publisher(parser=docutils.parsers.rst.Parser).get_settings()
        with open(src, encoding='utf-8') as f:
            self._document = new_document(
                source_path=src,
                settings=settings,
            )
            Parser().parse(f.read(), self.document)

    @property
    def document(self) -> Document:
        return self._document

    @document.setter
    def document(self, value):
        self._document = value
