==============
Directive Type
==============

The ``directive type`` is a string that specifies the type of directive.
**varST** supports all of directives for substitution in reStructuredText.

The example of directive type is following contents.

Replacement Text
================

Replacement Text is the most common type of directive.

.. code-block:: bash

   $ varst 'varST=reStructuredText'

The above command will update the substitution data of replacement text.

.. code-block:: diff

   - .. |varST| replace:: variable
   + .. |varST| replace:: reStructuredText

The substitution data of ``varST`` is updated to ``reStructuredText``.

Images
======

Image directive is used to insert images into the document.

.. code-block:: bash

   $ varst 'image url=https://example.com/new-image.png'

The above command will update the substitution data of image directive.

.. code-block:: diff

   - .. |image url| image:: https://example.com/old-image.png
   + .. |image url| image:: https://example.com/new-image.png

The substitution data of ``image url`` directive is updated to ``https://example.com/new-image.png``.

Objects
=======

Object directive is used to associate ambiguous text with a object identifier.

.. code-block:: bash

   $ varst 'isbn=9780738201443'

The above command will update the substitution data of object directive.

.. code-block:: diff

   - .. |isbn| book:: 0738201448
   + .. |isbn| book:: 9780738201443

The substitution data of ``isbn`` directive is updated to ``9780738201443``.
