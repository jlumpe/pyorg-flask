import os

import click
from flask.cli import FlaskGroup

from .factory import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
@click.option('-e', '--env', help='Set the Flask environment. Valid values are "production" (default) and "development".')
@click.option('--debug', is_flag=True, help='Run application in debug mode')
@click.pass_context
def cli(ctx, env, debug):
	"""Management script for the pyorg-flask application."""
	if env:
		os.environ['FLASK_ENV'] = env
	if debug:
		os.environ['FLASK_DEBUG'] = '1'
