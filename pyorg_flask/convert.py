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

		text_idx = 0
		for i, child in enumerate(elem.children):
			if 'org-header-text' in child.classes:
				test_idx = i
				break
		else:
			assert False

		button = self._make_elem_base('a', classes='pyorg-open-header', post_ws=True)
		elem.children.insert(text_idx + 1, button)

		return elem
