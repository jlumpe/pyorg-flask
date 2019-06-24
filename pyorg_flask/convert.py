"""Specialized HTML conversion for the web app."""

from pyorg.convert.html import OrgHtmlConverter


class PyorgFlaskHtmlConverter(OrgHtmlConverter):
	"""HTML converter for viewing an org file within the app."""
	DEFAULT_CONFIG = {
		**OrgHtmlConverter.DEFAULT_CONFIG
	}

	_convert_node = OrgHtmlConverter._convert_node.func.copy()
	_make_elem = OrgHtmlConverter._make_elem.func.copy()
