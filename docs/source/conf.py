import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Date Detection'
copyright = '2025, Mahmoud Lotfi'
author = 'Mahmoud Lotfi'
version = '1.0'
release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',           # ✅ Already compatible
    'sphinx.ext.napoleon',          # ✅ Perfect NumPy-style docs
    'sphinx.ext.viewcode',          # ✅ Will work excellently  
    'sphinx.ext.intersphinx',       # ✅ Cross-references ready
    'sphinx.ext.autosummary',       # ✅ Great for module overview
    'sphinx.ext.doctest',           # ✅ Can test example code
    'sphinx.ext.todo',              # ✅ Can include TODOs
    'sphinx.ext.coverage',          # ✅ Coverage reports
    'sphinx.ext.githubpages',       # For GitHub Pages deployment
    'myst_parser'                   # For Markdown support
]

# Napoleon configuration for docstrings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc configuration
autodoc_typehints = 'description'
autodoc_typehints_description_target = 'documented'
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Autosummary configuration
autosummary_generate = True
autosummary_imported_members = True

# Intersphinx mapping for cross-references
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'sklearn': ('https://scikit-learn.org/stable/', None),
}

# Add Markdown support
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# MyST parser configuration
myst_enable_extensions = [
    "deflist",
    "tasklist",
    "colon_fence",
    "attrs_inline",
    "attrs_block",
]

templates_path = ['_templates']
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**.ipynb_checkpoints'
]

# HTML output configuration
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'canonical_url': '',
    'analytics_id': '',
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_static_path = ['_static']
html_css_files = [
    'custom.css',  # Add custom CSS file
]

# Additional HTML context
html_context = {
    "display_github": True,
    "github_user": "your-username",
    "github_repo": "date-detection",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

# LaTeX output configuration (for PDF generation)
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'fncychap': '',
    'printindex': '',
}

# Grouping the document tree into LaTeX files
latex_documents = [
    ('index', 'DateDetection.tex', 'Date Detection Documentation',
     'Mahmoud Lotfi', 'manual'),
]

# Todo extension configuration
todo_include_todos = True
todo_emit_warnings = True

# Coverage configuration
coverage_show_missing_items = True