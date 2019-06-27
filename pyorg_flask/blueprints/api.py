"""Blueprint for REST api."""

from pathlib import Path

from flask import Blueprint, jsonify

from ..base import org
from pyorg.convert.json import to_json


api = Blueprint('api', __name__)


class ApiException(Exception):
	def __init__(self, code, message=None):
		self.code = code
		self.message = message


@api.errorhandler(ApiException)
def handle_api_error(err):
	data = {
		'code': err.code,
		'message': err.message,
	}
	return jsonify(data), err.code


from subprocess import CalledProcessError
from html import escape
@api.errorhandler(CalledProcessError)
def handle_emacs_error(err):
	stdout = escape(err.stdout.decode())
	stderr = escape(err.stdout.decode())
	return '<pre>%s</pre>\n<pre>%s</pre>' % (stdout, stderr)



def check_orgdir_path(path, exists=True, check_file=False, check_dir=False):
	path = Path(path)

	if path.is_absolute() or any(p.startswith('.') for p in path.parts[1:]):
		raise ApiException(404)

	abspath = org.orgdir.path / path

	if (exists and not abspath.exists()) or (check_file and not abspath.is_file()) or (check_dir and not abspath.is_dir()):
		raise ApiException(404)

	return path

def check_orgfile_path(path):
	path = check_orgdir_path(path, check_file=True)
	if path.suffix != '.org':
		raise ApiException(404)

	return path


@api.route('/files/orgfile/<string:path>')
def orgfile_contents(path):
	path = check_orgfile_path(path)
	node = org.read_org_file(path)
	contents = to_json(node)
	return jsonify({'path': str(path), 'contents': contents})


@api.route('/files/orgfile/<string:path>/open', methods=['POST'])
def open_orgfile(path):
	path = check_orgfile_path(path)
	org.open_org_file(path, focus=True)
	return '', 202


@api.route('/files/directory/')
@api.route('/files/directory/<string:path>')
def get_subdirectory(path=''):
	path = check_orgdir_path(path)
	contents = [str(f) for f in org.orgdir.list_files(path)]
	return jsonify({'path': str(path), 'contents': contents})


@api.route('/agenda')
def list_agenda():
	items = org.agenda(raw=True)
	return jsonify({'items': items})
