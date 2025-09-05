# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Eclipse Security Handbook'
copyright = '2024, Eclipse Foundation. Licensed under EPL-2.0'
author = 'Eclipse Foundation'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_design']

myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_logo = "_static/logo.svg"

html_theme_options = {
    "logo": {
        "text": "Security Handbook",
    },
    "github_url": "https://github.com/eclipse-csi/security-handbook",
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",
    # "show_nav_level": 2,
    "navbar_center": ["navbar-nav"],
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "footer_start": ["copyright"],
    "footer_center": ["sphinx-version"],
    "secondary_sidebar_items": {
        "**/*": ["page-toc", "edit-this-page", "sourcelink"]
    }
}

html_context = {
    "github_user": "eclipse-csi",
    "github_repo": "security-handbook",
    "github_version": "main",
    "doc_path": "docs"
}

html_sidebars = {
    'developer/*': ["sidebar-nav-bs"],
    "references/*": [],
}
