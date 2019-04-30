"""Global configuration for pytest tests."""

from pathlib import Path

import pytest


@pytest.fixture(name='test_data_dir', scope='module')
def get_test_data_dir():
	"""
	A :class:`pathlib.Path` object pointing to the directory containing test
	data.
	"""
	test_dir = Path(__file__).parent
	return test_dir.joinpath('testdata').absolute()
