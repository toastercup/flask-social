from flask.ext.restful import fields

image_fields = {
    'cdn_guid': fields.String,
    'title' : fields.String,
    'description' : fields.String,
    'updated' : fields.DateTime
}
