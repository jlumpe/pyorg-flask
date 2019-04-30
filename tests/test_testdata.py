"""Test that we can load test data (meta-testing!)"""


def test_test_data_dir(test_data_dir):

	# Make sure the directory exists
	assert test_data_dir.is_dir()

	# Read and check the contents
	example = test_data_dir / 'example.txt'
	with example.open() as fobj:
		contents = fobj.read()

	assert contents.strip() == 'Example data file for meta-testing'
