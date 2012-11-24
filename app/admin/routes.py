from flask import Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.before_request
def restrict_bp_to_admins():
    if False:
        return "buh"