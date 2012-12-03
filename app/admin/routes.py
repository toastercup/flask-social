from app import admin

@admin.before_request
def restrict_bp_to_admins():
    if False:
        return "buh"