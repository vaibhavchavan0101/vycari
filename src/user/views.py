import os
import subprocess

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token

from .serializers import LoginSerializer, UserSerializer, ForgotPasswordSerializer
from .swagger_decorators import login_schema, register_schema, forgot_password_schema

User = get_user_model()

class LoginView(APIView):
    @login_schema
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserView(viewsets.ViewSet):
    serializer_class = UserSerializer
    @register_schema
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    @forgot_password_schema
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'message': 'User does not exist.'}, status=status.HTTP_400_BAD_REQUEST)

            # Generate password reset token
            token_generator = PasswordResetTokenGenerator()
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            BASE_URL = request.build_absolute_uri('/')[:-1]
            reset_link = f"{BASE_URL}/api/reset-password/confirm/{uid}/{token}"
            try:
                # Send password reset email
                send_mail(
                    'Reset Your Password',
                    f'Click the link to reset your password: {reset_link}',
                    os.environ.get('EMAIL_HOST_USER'),
                    [email],
                    fail_silently=False,
                )
            except:
                return Response({'message': 'SMTP Authentication is required'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({'message': 'Password reset link has been sent to your email.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_email_notification_for_git_push():
    """ Send email notification for each git push using Git's pre-push hooks. """

    branch_name = subprocess.check_output(
        ['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode('utf-8').strip()
    commit_details = subprocess.check_output(
        ['git', 'log', '-1']).decode('utf-8').strip()
    email = subprocess.check_output(
        ['git', 'config', 'user.email']).decode('utf-8').strip()
    user = subprocess.check_output(
        ['git', 'config', 'user.name']).decode('utf-8').strip()
    subject = f'Git Push - by {user} for branch "{branch_name}" '
    message = f'Git push details:\n{commit_details}\n\nBranch name: {branch_name}\nEmail: {email}\nUser: {user}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['apurvnagrale@gmail.com']
    send_mail(subject, message, from_email, recipient_list)
    return