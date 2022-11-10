import importlib.metadata

_PROJECT_METADATA = importlib.metadata.metadata('varst')

project = _PROJECT_METADATA['Name']
author = _PROJECT_METADATA['Author']
release = _PROJECT_METADATA['Version']
copyright = f'2022, {project}'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_search.extension',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_title = f'varST documentation v{release}'
html_static_path = ['_static']
