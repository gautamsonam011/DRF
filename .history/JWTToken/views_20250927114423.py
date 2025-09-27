from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token



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

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({
                'error':'Please provide both username and password'
            }, status = status.HTTP_400_BAD_REQUEST)

        user = authenticate(username = username, password = password)

        if not user:
            return Response({'error': "Invalid credentials"}, status = status.HTTP_401_UNAUTHORIZED)

            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})      
     
            