from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from account.serializers import UserSerializer, UserRegistrationSerializer,UserLoginSerializer
from account.models import UserAccount
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated



########### SEND EMAIL ###########
def send_email(user,confirm_link, mail_subject,template):
    message = render_to_string(template, {
        'user': user,
        'link': confirm_link,
    })
    from_email = "TICKETEXPRESS <delwarjnu24@gmail.com>"
    send_email = EmailMultiAlternatives(mail_subject, '', to=[user.email], from_email=from_email, reply_to=[from_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

# Create your views here.
class UserListViewSet(viewsets.ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    

class UserRegistrationViewSet(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer_form = self.serializer_class(data=request.data)

        if serializer_form.is_valid():
            user = serializer_form.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f'http://127.0.0.1:8000/account/activate/{uid}/{token}'
            send_email(user, confirm_link, 'Email Verification Message', 'email.html')
            return Response({"error": False, "message": "we have sent a verification email, please verify your email"})
        return Response(serializer_form.errors)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = UserAccount._default_manager.get(pk=uid)
    except UserAccount.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # return JsonResponse({'success': True, 'message': 'Email verification successful'})
        return redirect('http://localhost:5173/login')
    else:
        return JsonResponse({'success': False, 'message': 'Invalid activation link'})

  
class UserLoginViewSet(APIView):
    serializer_class =UserLoginSerializer
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, _create = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credentials'}, status=401)
        else:
            return Response({'error': serializer.errors}, status=400)
        
class UserLogoutViewSet(APIView):
    def get(self, request, *args, **kwargs):
        if request.auth:  
            request.auth.delete()
        logout(request)
        return Response({'detail': 'Logout successful'},status=status.HTTP_200_OK)

        




