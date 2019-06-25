"""Blueprint for viewing (org and non-org) files in the org directory."""

import os
from pathlib import Path
from subprocess import CalledProcessError

from flask import (
	Blueprint, render_template, Markup, send_file, abort, url_for, redirect,
	current_app, request
)
import jinja2


from pyorg.ast import OrgNode

from ..base import org
from ..convert import PyorgFlaskHtmlConverter


files_bp = Blueprint('files', __name__, template_folder='../templates')



def file_link_resolver(orgdir, wd=None):
	orgdir = Path(orgdir).expanduser()
	wd = None if wd is None else Path(wd).absolute()

	def resolver(linktype, raw, path, ctx=None):
		path2 = Path(os.path.normpath(path)).expanduser()
		if not path2.is_absolute():
			if wd is not None:
				path2 = (wd / path2).resolve()
			else:
				return None

		try:
			relpath = path2.relative_to(orgdir)
		except ValueError:
			# Not in org directory
			return None

		assert not str(relpath).startswith('/')
		assert not str(relpath).startswith('.')

		return url_for('pyorg.viewfile', path=str(relpath))

	return resolver


def get_converter(orgdir=None, wd=None):
	"""Get configured HTML converter.

	Parameters
	----------
	orgdir
		Absolute path to org directory.
	wd
		Working directory, for resolving file links.

	Returns
	-------
	pyorg.html.OrgHtmlConverter
	"""
	resolve_link = {}

	if orgdir is not None and wd is not None:
		resolve_link['file'] = file_link_resolver(orgdir, wd)

	config = dict(
		resolve_link=resolve_link,
	)
	return PyorgFlaskHtmlConverter(config)


def convert_org_data(data, **kw):
	"""Convert org file data to raw HTML."""
	converter = get_converter(**kw)
	return converter.convert(data)


@files_bp.context_processor
def context_processor():
	return dict(
		favorite_files=current_app.config.get('ORG_FAVORITE_FILES', []),
	)

@jinja2.contextfilter
@files_bp.app_template_test('orgnode')
def test_orgast(value):
	return isinstance(value, OrgNode)


@files_bp.errorhandler(CalledProcessError)
def handle_emacs_error(exc):
	return render_template('emacs-error.html.j2', exc=exc)


@files_bp.route('/')
@files_bp.route('/<path:path>')
def viewpath(path=''):
	if not path or path.endswith('/'):
		return view_org_directory(path)

	if path.endswith('.org'):
		return view_org_file(path)

	return get_other_file(path)


def _make_toc(node):
	return (node.title, node.id, list(map(_make_toc, node.outline_children)))

def make_toc(root):
	return list(map(_make_toc, root.outline_children))

def view_org_file(path):

	path = Path(path)
	abspath = org.orgdir.get_abs_path(path)

	if not abspath.is_file():
		return render_template('orgfile-404.html.j2', file=str(path)), 404

	content = org.read_org_file(path, assign_ids=True)
	toc = make_toc(content)

	# Display AST
	if request.args.get('show', '').lower() == 'ast':
		return render_template(
			'orgfile-ast.html.j2',
			ast=content,
			file_name=path.name,
			parents=path.parent.parts,
			toc=toc,
		)

	html = convert_org_data(content, wd=abspath.parent, orgdir=org.orgdir.path)

	return render_template(
		'orgfile.html.j2',
		ast=content,
		file_content=Markup(html),
		file_name=path.name,
		file_title=content.title or abspath.stem,
		parents=path.parent.parts,
		# source_json=json.dumps(data, indent=4, sort_keys=True),
		toc=toc,
	)


def view_org_directory(path):
	path = Path(path)
	abspath = org.orgdir.get_abs_path(path)

	dirs = []
	files = []

	for item in abspath.iterdir():
		if item.name.startswith('.'):
			continue

		if item.is_dir():
			dirs.append(item.name)

		if item.is_file() and item.name.endswith('.org'):
			files.append(item.name)

	*parents, dirname = ['root', *path.parts]

	return render_template(
		'dirindex.html.j2',
		dirname=dirname,
		dirs=dirs,
		files=files,
		parents=parents,
	)


def get_other_file(filepath):
	abspath = org.orgdir.get_abs_path(filepath)

	if not abspath.exists():
		abort(404)

	if abspath.is_dir():
		return redirect(url_for('pyorg.viewfile', path=filepath + '/'))

	return send_file(str(abspath))
