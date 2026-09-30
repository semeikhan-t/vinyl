from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class TokenBlacklistView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()
            return Response({})        
        except Exception as e:
            return Response({"error": e}, status=400)
