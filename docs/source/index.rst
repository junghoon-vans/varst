=======================
var ➡️ reStructuredText
=======================

Replace substitutions in rst files with variables.

Quickstart
==========

Installation
------------

To install **varST**, run this command.

.. code:: bash

   $ pip install varst

Usage
-----

.. code:: bash

   $ varst [-i INPUT] [-o OUTPUT] [substitutions ...]

   # run with default input and output
   $ varst 'name=value'

   # run with custom input and output
   $ varst -i input.rst -o output.rst 'name=value'

   # run with multiple substitutions
   $ varst 'name1=value1' 'name2=value2'

Github Actions
==============

varST can be integrated with ``Github Actions``.
Please refer to this link_ and apply it to your own workflows.


API documentation
=================

.. toctree::
   :maxdepth: 2

   api/varst

Changelog
=========

.. toctree::
   :maxdepth: 2

   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`


.. _link: https://github.com/marketplace/actions/rst-substitution
