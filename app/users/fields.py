from flask.ext.restful import fields

user_fields = {
    'email': fields.String,
    'name' : fields.String,
    'status' : fields.String,
    'role' : fields.String
}
