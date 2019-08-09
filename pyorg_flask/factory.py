"""Application factory."""

import os

from flask import Flask, render_template

from pyorg.emacs import EmacsException


#: Default location of the config file
DEFAULT_CONFIG_PATH = '~/.pyorg-config.py'


def create_app(config_file=None, config=None):
	"""Create the pyorg Flask application object.

	Parameters
	----------
	config_file : str
		Config file to load. Otherwise use PYORG_CONFIG environment variable.
	config : dict
		Dictionary with additional configuration.

	Returns
	-------
	flask.Flask
	"""
	app = Flask(__package__)

	# Default configuration
	app.config.from_object(__package__ + '.config_default')

	# User config file - from argument, environment variable, or default
	silent = False
	if config_file is None:
		config_file = os.environ.get('PYORG_CONFIG')
	if config_file is None:
		config_file = DEFAULT_CONFIG_PATH
		silent = True
	app.config.from_pyfile(os.path.expanduser(config_file), silent=silent)

	# Update from supplied mapping
	if config is not None:
		app.config.from_mapping(config)

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

	# Imports for shell context
	@app.shell_context_processor
	def shell_context():
		from .base import emacs, org
		return dict(emacs=emacs, org=org)

	return app
