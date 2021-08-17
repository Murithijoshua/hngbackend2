from rest_framework import serializers
from .models import Entrys


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrys
        fields = '__all__'
