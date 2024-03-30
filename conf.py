project = 'Mon Angular Fire'
copyright = '2043, on'
author = 'on'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_favicon = 'https://storage.googleapis.com/idf-congestion/favicon.ico'
html_static_path = ['_static']
html_show_copyright = False
html_show_sphinx = False
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logo.png",
    "dark_logo":  "logo.png",
}
