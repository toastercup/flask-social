from flask.ext.restful import Resource, marshal_with

from social.images import fields
from social.images.models import Image
from social.decorators import requires_auth


# TODO: Create wrapper around simples3
class ImagesResource(Resource):
    @requires_auth
    def get(self):
        images = Image.query.all()

        imagesDict = {}
        for image in images:
            imagesDict[image.id] = {
                'cdn_guid': image.cdn_guid,
                'description': image.description,
                'title': image.title,
                'updated': str(image.updated),
                'user': image.user
            }

        return imagesDict


class ImageResource(Resource):
    @requires_auth
    @marshal_with(fields.image_fields)
    def get(self, image_id):
        image = Image.query.filter_by(id=image_id).first_or_404()

        return image


class NewImageResource(Resource):
    @requires_auth
    @marshal_with(fields.image_fields)
    def get(self, image_id):
        image = Image.query.filter_by(id=image_id).first()

        return image
