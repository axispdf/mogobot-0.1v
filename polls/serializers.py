from dataclasses import field
from rest_framework import serializers

from .models import Urls


class SerializeUrls(serializers.Serializer):
    '''Список ссылок'''


    class Meta:
        model = Urls
        field = '__all__'


