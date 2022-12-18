==============================
varST(var ➡️ reStructuredText)
==============================

|PyPI version| |Github Actions| |pre-commit.ci status| |GitHub Workflow Status| |Documentation Status|

Replace substitutions in rst files with variables.

Installation
============

.. code:: bash

   $ pip install varst

Usage
=====

Command
-------

.. code:: bash

   $ varst [-i INPUT] [-o OUTPUT] [name=value ...]

Github Actions
--------------

varST can be integrated with ``Github Actions``.
Please refer to this link_ and apply it to your own workflows.

License
=======

`MIT
License <https://github.com/junghoon-vans/varst/blob/main/LICENSE>`__

.. |PyPI version| image:: https://img.shields.io/pypi/v/varst
   :target: https://pypi.org/project/varst/
.. |Github Actions| image:: https://img.shields.io/badge/Actions-black?logo=github
   :target: https://github.com/marketplace/actions/rst-substitution
.. |pre-commit.ci status| image:: https://results.pre-commit.ci/badge/github/junghoon-vans/varst/main.svg
   :target: https://results.pre-commit.ci/latest/github/junghoon-vans/varst/main
.. |GitHub Workflow Status| image:: https://img.shields.io/github/actions/workflow/status/junghoon-vans/varst/python-deploy.yml?branch=v1.2.0
.. |Documentation Status| image:: https://readthedocs.org/projects/varst/badge/?version=latest
    :target: https://varst.readthedocs.io/en/latest/?badge=latest

.. _link: https://github.com/marketplace/actions/rst-substitution
