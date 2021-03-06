"""Default configuration file for pyorg flask app."""


# Root org directory (defaults to value of `org-directory` in Emacs)
# PYORG_ORG_DIRECTORY = '~/org'

# Base command to run Emacs in non-interactive mode
# PYORG_EMACS_CMD = ['emacs', '--batch']
PYORG_EMACS_CMD = ['emacsclient']

# Whether PYORG_EMACS_CMD is running emacsclient
PYORG_EMACS_IS_CLIENT = True

# List of favorite files (relative to org directory).
PYORG_FAVORITE_FILES = []

# Shell to use for the "shell" CLI command. "builtin" to use Python's builtin REPL,
# "ipython" to use IPython if installed.
PYORG_SHELL = 'builtin'


# Raw HTML to insert at the end of the <head> element on every page.
# You can use this to insert custom CSS or Javascript or configure MathJax
# PYORG_HTML_HEAD = '''\
# <!-- MathJax configuration -->
# <script type="text/x-mathjax-config">
# 	MathJax.Hub.Config({
# 		TeX: {
# 			Macros: {
# 				"MyCustomMacro": ["\\boldsymbol{#1}", 1],
# 			}
# 		}
# 	});
# </script>
# '''
