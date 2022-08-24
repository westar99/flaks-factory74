from flask import Blueprint, render_template

bp = Blueprint('dashapp1',
                __name__,
                template_folder = 'templates',
                url_prefix="/dashapp1")

@bp.route('/',methods=['GET'])
def main():
    return render_template('dashapp1.jinja2',title="Main Page")