from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializers import *
from rest_framework.response import Response

class VMView(APIView):
    def get(self, request):
        output = [{"nameVM": vm.nameVM}
                   for vm in VM.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = VMSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)