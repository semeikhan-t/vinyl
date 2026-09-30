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

class AuthMeView(APIView):
    def get(self, request):
        try:
            username = request.user.username
            email = request.user.email
            return Response({"username": username, "email": email})
        except Exception as e:
            return Response({"error": e}, status=400)
    
    def patch(self, request):
        try:
            email_new = request.data.get("email").lower().strip()
            username_new = f'{request.data.get("username")}'.lower().strip()
            if username_new.find(' ') > 0:
                return Response({
                    "code": "invalid", 
                    "detail":"Validation failed.", 
                    "fields": {"username":["This field may not contain spaces."]}},
                    status = 400)
            request.user.email = email_new
            request.user.save()
            request.user.username = username_new
            request.user.save()
            return Response({"username": username_new, "email": email_new})
        except Exception as e:
            return Response({"error": e}, status=400)
