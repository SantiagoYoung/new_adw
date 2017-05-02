from rest_framework import serializers
from .models import *


class SystemInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemInformation
        fields = ('id', 'title', 'message','username')