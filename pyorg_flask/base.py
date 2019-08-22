from flask import current_app, g
from werkzeug.local import LocalProxy

import os


def get_emacs():
	"""Get ``Emacs`` instance to use with application context.

	Returns
	-------
	pyorg.emacs.Emacs
	"""
	if 'emacs' not in g:
		from emacs import Emacs

		g.emacs = Emacs(
			cmd=current_app.config.get('PYORG_EMACS_CMD'),
			client=current_app.config.get('PYORG_EMACS_IS_CLIENT', False),
		)

	return g.emacs


def get_org():
	"""Get ``Org`` instance to use with application context.

	Returns
	-------
	pyorg.emacs.Org
	"""
	if 'org' not in g:
		from pyorg import Org
		from pyorg.interface import OrgFilesystemCache

		g.org = Org(
			emacs=get_emacs(),
			orgdir=current_app.config.get('PYORG_ORG_DIRECTORY'),
		)

		cache_dir = os.path.join(current_app.config['PYORG_DIR'], 'cache')
		g.org.loader = OrgFilesystemCache(g.org.orgdir, cache_dir, g.org.emacs)

	return g.org


emacs = LocalProxy(get_emacs)
org = LocalProxy(get_org)
