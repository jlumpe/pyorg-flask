"""Blueprint for viewing agenda entries."""

from flask import Blueprint, render_template
from pyorg.convert.html import OrgHtmlConverter

from ..base import org


bp = Blueprint('agenda', __name__, template_folder='../templates')



@bp.route('/')
def agenda():

	items = org.agenda()

	converter = OrgHtmlConverter()

	for item in items:
		item['text_html'] = converter.make_headline_text(item['node'])

	items.sort(key=lambda item: (-item['priority'], item['file-relative'], *item['path']))

	return render_template(
		'agenda.html.j2',
		items=items,
		converter=converter,
	)
