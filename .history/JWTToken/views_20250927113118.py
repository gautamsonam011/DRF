from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username = username).exists():
            return Response({'error':'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username = username, password = password)

        # Generate token manually 

        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'User registered successfully',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

class ProtectedView(APIView):
    permission_classes =[IsAuthenticated]

    def get(sefl, request):
        return Response({'message': f'Hello, {request.user.username}! This is protected.'})


     
            