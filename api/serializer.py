from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Images


class ImageSerializer(ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url', read_only=True)

    class Meta:
        model = Images
        fields = ('id', 'name', 'author', 'image', 'image_url')
        read_only_fields = ('id', 'author')

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)
