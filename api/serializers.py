from rest_framework import serializers

from .models import Employee


class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('fullname', 'position')
