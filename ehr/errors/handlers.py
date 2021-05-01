from flask import render_template, Blueprint

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
	return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
	return render_template('errors/403.html'), 403


@errors.app_errorhandler(505)
def error_405(error):
	return render_template('errors/505.html'), 505