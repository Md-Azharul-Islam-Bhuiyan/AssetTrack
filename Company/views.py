from django.shortcuts import render, redirect
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from Company.serializers import RegistrationSerializer, LoginSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout


# Define for user registration.
class RegistrationView(APIView):
    serializer_class = RegistrationSerializer
     # Define the POST method to handle user registration.
    def post(self, request):
        try:
             # Create a serializer instance with the request data.
            serializer = self.serializer_class(data=request.data)
            
            # Check if the serializer data is valid.
            if serializer.is_valid():
                user = serializer.save()
                # Generate a token for email confirmation.
                token = default_token_generator.make_token(user)
                # Encode the user's primary key
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                confirm_link = f"http://127.0.0.1:8000/company/active/{uid}/{token}"

                email_subject = "Confirm Your Email"
                email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            
                email = EmailMultiAlternatives(email_subject , '', to=[user.email])
                email.attach_alternative(email_body, "text/html")
                email.send()

                return Response({'success': True, 'message': 'Registration Successful. Please check your email.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({
                    'success': False,
                    'message': 'Failed to registered. Data is not valid',
                    'status':status.HTTP_400_BAD_REQUEST
                })
        except Exception as e:
            return Response({'message':'Failed to registered','error':e,"status": status.HTTP_500_INTERNAL_SERVER_ERROR})


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User.objects.get(pk=uid)
    
    except User.DoesNotExist:
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        
        user.save()

        return redirect("register")
    else:
        return redirect("register")



class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data= self.request.data)

        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]

            user = authenticate(username = username, password = password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({
                        "success": True,
                        'message': "Successfully logged in!!!",
                        "token": token.key,
                        'status':status.HTTP_200_OK
                })
            else:
                return Response({
                "success": False,
                "message": "Invalid Credentials",
                "status" : status.HTTP_401_UNAUTHORIZED
        })
        return Response(serializer.errors)
    

class LogoutView(APIView):
    
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect("login")
            
        
        