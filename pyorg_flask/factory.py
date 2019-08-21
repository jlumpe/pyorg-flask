"""Application factory."""

import os

from flask import Flask, render_template, current_app

from emacs import EmacsException


#: Default location of the application directory
DEFAULT_APP_DIR = '~/.pyorg'


def locate_app_dir(path=None):
	"""Locate the application directory.

	Parameters
	----------
	path : str
		Optional, overrides default method of finding application directory and
		just returns the argument (after normalizing) if given. If None will
		attempt to get from ``PYORG_DIR`` environment variable, followed by
		:data:`.DEFAULT_APP_DIR`.

	Returns
	-------
	str
	"""
	if path is None:
		path = os.environ.get('PYORG_DIR', DEFAULT_APP_DIR)
	return os.path.abspath(os.path.expanduser(path))


def create_app(app_dir=None, config=None):
	"""Create the pyorg Flask application object.

	Parameters
	----------
	app_dir : str
		Path to application directory. See :func:`.locate_app_dir`.
	config : dict
		Dictionary with additional configuration.

	Returns
	-------
	flask.Flask
	"""
	app = Flask(__package__)

	# Find application directory
	app_dir = locate_app_dir(app_dir)
	if not os.path.isdir(app_dir):
		raise NotADirectoryError(app_dir)

	app.config['PYORG_DIR'] = app_dir

	# Default configuration
	app.config.from_object(__package__ + '.config_default')

	# User config file in application directory
	app.config.from_pyfile(os.path.join(app_dir, 'config.py'))

	# Update from supplied mapping
	if config is not None:
		app.config.from_mapping(config)

	setup_app(app)

	return app


def setup_app(app):
	"""Set up an existing application object.

	Parameters
	----------
	app : flask.Flask
		Existing application with configuration applied.
	"""
	# Register blueprints
	from .blueprints.core import bp as core_bp
	app.register_blueprint(core_bp, url_prefix='/')
	from .blueprints.files import bp as files_bp
	app.register_blueprint(files_bp, url_prefix='/files')
	from .blueprints.agenda import bp as agenda_bp
	app.register_blueprint(agenda_bp, url_prefix='/agenda')
	from .blueprints.api import api
	app.register_blueprint(api, url_prefix='/api')

	# Handle errors in Emacs interface
	@app.errorhandler(EmacsException)
	def handle_emacs_exception(exc):
		return render_template('emacs-error.html.j2', exc=exc), 500

	# Template environment
	@app.context_processor
	def context_processor():
		return dict(
			user_head=current_app.config.get('PYORG_HTML_HEAD')
		)

	# Imports for shell context
	@app.shell_context_processor
	def shell_context():
		from .base import emacs, org
		return dict(emacs=emacs, org=org)
