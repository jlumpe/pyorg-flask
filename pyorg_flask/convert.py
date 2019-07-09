"""Specialized HTML conversion for the web app."""

from pyorg.convert.html import OrgHtmlConverter


class PyorgFlaskHtmlConverter(OrgHtmlConverter):
	"""HTML converter for viewing an org file within the app."""
	DEFAULT_CONFIG = {
		**OrgHtmlConverter.DEFAULT_CONFIG
	}

	_convert_node = OrgHtmlConverter._convert_node.func.copy()
	_make_elem = OrgHtmlConverter._make_elem.func.copy()

	def _make_headline(self, headline, ctx):
		elem = super()._make_headline(headline, ctx)
		button = self._make_elem_base('a', classes='pyorg-open-header', post_ws=True)
		elem.children.append(button)
		return elem
