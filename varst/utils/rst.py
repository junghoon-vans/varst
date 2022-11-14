import docutils
from docutils.core import publish_from_doctree
from docutils.core import Publisher
from docutils.nodes import document as Document
from docutils.nodes import Element
from docutils.nodes import Node
from docutils.nodes import Text
from docutils.parsers.rst import Parser
from docutils.utils import new_document
from docutils_rst_writer import Writer as RstWriter


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

    def substitution_def_node(self, name: str) -> Element:
        """Find substitution definition node by name.

        Args:
            name: The string value of substitution name.
        Returns:
            Element: The node object what define substitution.

        """
        return self.document.substitution_defs[name]

    def substitution_text(self, name: str) -> Node:
        """Find substitution text by name.

        Args:
            name: The string value of substitution name.
        Returns:
            Node: The node object of substitution text.

        """
        return self.substitution_def_node(name).next_node()

    def replace_substitution(self, name: str, value: str) -> None:
        """Replace substitution text with name to value.

        Args:
            name: The string value of substitution name.
            value: The string value of substitution text.

        """
        def_node: Element = self.substitution_def_node(name)
        text_node: Node = self.substitution_text(name)

        def_node.replace(
            old=text_node,
            new=Text(value),
        )

    def save(self, dest: str) -> None:
        """Save the document object to the destination path as rst file.

        Args:
            dest: The string value of destination path.

        """
        output = publish_from_doctree(self.document, writer=RstWriter())
        with open(dest, encoding='utf-8', mode='w') as f:
            f.write(str(output, 'utf-8'))
