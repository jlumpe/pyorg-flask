"""Setuptools installation script for pyorg-flask package."""

from setuptools import setup
import re


# Get contents of README file
with open('README.md') as fh:
	readme_contents = fh.read()


# Read version from root module __init__.py
with open('pyorg_flask/__init__.py') as fh:
	init_contents = fh.read()
	version_match = re.search('^__version__ = ["\']([^"\']+)["\']', init_contents, re.M)

	if not version_match:
		raise RuntimeError('Unable to get version string')

	version = version_match.group(1)



requirements = [
	'pyorg',
	'Flask~=1.0',
]

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']


setup(
	name='pyorg-flask',
	version=version,
	description='Flask app for pyorg package.',
	long_description=readme_contents,
	author='Jared Lumpe',
	author_email='mjlumpe@gmail.com',
	url='https://github.com/jlumpe/pyorg-flask',
	python_requires='>=3.5',
	install_requires=requirements,
	setup_requires=setup_requirements,
	tests_require=test_requirements,
	include_package_data=True,
	dependency_links=['http://github.com/jlumpe/pyorg/tarball/master'],
	# license='',
	# classifiers='',
	# keywords=[],
	# platforms=[],
	# provides=[],
	# requires=[],
	# obsoletes=[],
)
