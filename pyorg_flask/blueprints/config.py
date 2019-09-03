"""Blueprint for app configuration."""

from flask import Blueprint, render_template, url_for, redirect, flash

from ..base import org


bp = Blueprint('config', __name__, template_folder='../templates')


@bp.route('/')
def menu():
	return render_template('config.html.j2')


@bp.route('/clear-cache', methods=['POST'])
def clear_cache():
	cache = org.loader
	flash('Cleared %d cached org files.' % len(cache))
	cache.clear()
	return redirect(url_for('config.menu'))
