from django.contrib.auth.password_validation import validate_password as validate_password_strength
from rest_framework import serializers

from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def validate_email(self, value):
        email = value.strip().lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Account with this email already exists!")
        return email

    def validate_password(self, value):
        validate_password_strength(value)
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        