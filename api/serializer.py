from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Images


class ImageSerializer(ModelSerializer):

    class Meta:
        model = Images
        fields = ('id', 'name', 'author', 'image')
        read_only_fields = ('id', 'author')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)
