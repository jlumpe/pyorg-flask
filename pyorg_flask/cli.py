import os
from shutil import rmtree
import logging

import click
from flask import current_app
from flask.cli import FlaskGroup, with_appcontext, shell_command as flask_shell

from .factory import create_app, locate_app_dir, init_app_dir


LOG_LEVELS = ['debug', 'info', 'warning', 'error', 'critical']


@click.group(cls=FlaskGroup, create_app=create_app)
@click.option('-e', '--env', help='Set the Flask environment. Valid values are "production" (default) and "development".')
@click.option('--debug', is_flag=True, help='Run application in debug mode')
@click.option('-d', '--app-dir', help='Path to application directory')
@click.option('--log', '-l', 'loglevel', type=click.Choice(LOG_LEVELS),
              help='Set logging level')
@click.option('-v', 'verbosity', count=True,
              help='Increase verbosity level. Use once for info, twice for debug.')
@click.pass_context
def cli(ctx, env, debug, app_dir, loglevel, verbosity):
	"""Management script for the pyorg-flask application."""
	if env:
		os.environ['FLASK_ENV'] = env
	if debug:
		os.environ['FLASK_DEBUG'] = '1'
	if app_dir:
		os.environ['PYORG_DIR'] = app_dir

	# Configure logging
	logging.basicConfig(format='%(levelname)s[%(name)s]: %(message)s')

	if loglevel is None:
		if verbosity == 1:
			loglevel = 'info'
		elif verbosity > 1:
			loglevel = 'debug'

	if loglevel is not None:
		level = getattr(logging, loglevel.upper())
		logging.getLogger('pyorg_flask').setLevel(level)


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


@cli.group('config')
def config_group():
	"""Manage app configuration."""


@config_group.command('locate', with_appcontext=False)
def locate_app_dir_command():
	"""Get the path the application directory is expected to be found at."""
	click.echo(locate_app_dir())


@config_group.command('print')
def print_config_command():
	"""Print the application configuration values."""
	from pprint import pprint
	stdout = click.get_text_stream('stdout')
	w, h = click.get_terminal_size()

	for key in sorted(current_app.config):
		value = current_app.config[key]
		click.echo(key + ' = ', nl=False)
		pprint(value, stdout, width=w)


@config_group.command('init', with_appcontext=False)
@click.argument('path', required=False)
@click.option('-f', '--force', is_flag=True, help='Overwrite existing directory.')
@click.option('-d', '--dry-run', is_flag=True,
              help="Don't actually do anything, only print what would be done.")
def init_app_dir_command(path, force, dry_run):
	"""Create a fresh application directory with default configuration."""
	if path is None:
		path = locate_app_dir()

	# Directory exists
	if os.path.exists(path):
		if force:
			if not dry_run:
				rmtree(path)
		else:
			raise click.ClickException(
				'Directory %s already exists. Use --force option to overwrite.'
				% path)

	# Create directory and copy config file
	click.echo('Creating application directory at %s' % os.path.abspath(path))

	if not dry_run:
		init_app_dir(path)
