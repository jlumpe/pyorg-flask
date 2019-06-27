"""Blueprint for core application pages, e.g. home page."""

from flask import Blueprint, render_template


bp = Blueprint('core', __name__, template_folder='../templates')


# Routes
@bp.route('/')
def home():
	return render_template('home.html.j2')
