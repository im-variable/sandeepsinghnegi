from django.shortcuts import render
from rest_framework.views import APIView
from . serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    
    def post(self, request):
        """
        for registering user
        """
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        for get registered user
        """
        qs = User.objects.all()
        serializer = RegisterSerializer(qs, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)