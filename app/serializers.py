from rest_framework import serializers
from . models import *

class VMSerializer(serializers.ModelSerializer):
    class Meta:
        model = VM
        fields = ['nameVM']