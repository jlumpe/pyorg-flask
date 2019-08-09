import os

import click
from flask import current_app
from flask.cli import FlaskGroup, with_appcontext, shell_command as flask_shell

from .factory import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
@click.option('-e', '--env', help='Set the Flask environment. Valid values are "production" (default) and "development".')
@click.option('--debug', is_flag=True, help='Run application in debug mode')
@click.option('-c', '--config', help='Location of config file')
@click.pass_context
def cli(ctx, env, debug, config):
	"""Management script for the pyorg-flask application."""
	if env:
		os.environ['FLASK_ENV'] = env
	if debug:
		os.environ['FLASK_DEBUG'] = '1'
	if config:
		os.environ['PYORG_CONFIG'] = config


def ipython_shell():
	"""Run the IPython shell.

	This handles the condition of IPython not being installed gracefully.

	Returns
	-------
	bool
		True if IPython was successfully imported and the shell run, False otherwise.
	"""
	try:
		from IPython import start_ipython
	except ImportError as exc:
		click.echo('Error importing IPython, falling back to builtin shell: %s' % exc)
		return False

	ctx = current_app.make_shell_context()

	from traitlets.config import Config
	c = Config()
	c.InteractiveShell.banner2 = "App: %s [%s]\nInstance: %s" % (
		current_app.import_name,
		current_app.env,
		current_app.instance_path,
	)

	start_ipython(argv=[], user_ns=ctx, config=c)

	return True


@cli.command("shell", short_help=flask_shell.short_help, help=flask_shell.help)
@click.option('--builtin', 'shell', flag_value='builtin', help='Use Python\'s builtin REPL.')
@click.option('--ipython', 'shell', flag_value='ipython', help='Use IPython.')
@click.pass_context
@with_appcontext
def shell_command(ctx, shell):
	"""Overrides the builtin Flash shell command to allow using IPython."""

	if shell is None:
		shell = current_app.config.get('PYORG_SHELL', 'builtin')

	if shell.lower() == 'ipython':
		if ipython_shell():
			return

	elif shell.lower() != 'builtin':
		click.echo('Unrecognized shell option %r, falling back to builtin' % shell, err=True)

	# Run default version of command.
	ctx.invoke(flask_shell)
