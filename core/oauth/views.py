from django.shortcuts import redirect
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated

from .models import (
    ApplicationClient,
    AuthorizationCode,
    ClientSecret,
)

class OAuth2AuthorizeView(APIView):
    def get(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return redirect(f'/auth/login/?next={request.path}')
        
        # Check if client_id is provided
        client_id = request.GET.get('client_id')
        if not client_id:
            raise APIException('client_id is required')
        
        # Check if client_id exists
        try:
            client = ApplicationClient.objects.get(client_id=client_id)
        except ApplicationClient.DoesNotExist:
            raise APIException('Invalid client_id')
        
        # Check if client is authorized
        if request.user != client.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        # Check if redirect_uri is provided
        redirect_uri = request.GET.get('redirect_uri')
        if not redirect_uri:
            raise APIException('redirect_uri is required')
        
        # Check if redirect_uri is authorized
        authorized_redirect_uris = client.authorized_redirect_uris.split(',')
        if redirect_uri not in authorized_redirect_uris:
            raise APIException('Invalid redirect_uri')
        
        # Generate authorization code
        code = AuthorizationCode.objects.create(client=client)

        # Redirect to redirect_uri with code
        return redirect(f'{redirect_uri}?code={code}'.format(
                redirect_uri=redirect_uri,
                code=code.code
            )
        )
            
class OAuth2TokenView(APIView):
    #permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        # Check if client_id is provided
        client_id = request.data.get('client_id')
        if not client_id:
            raise APIException('client_id is required')
        
        # Check if client_id exists
        try:
            client = ApplicationClient.objects.get(client_id=client_id)
        except ApplicationClient.DoesNotExist:
            raise APIException('Invalid client_id')
        
        # Check if client is authorized
        if request.user != client.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        # Check if code is provided
        code = request.data.get('code')
        if not code:
            raise APIException('code is required')
        
        # Check if code exists
        try:
            code = AuthorizationCode.objects.get(code=code)
        except AuthorizationCode.DoesNotExist:
            raise APIException('Invalid code')
        
        # Check if code is valid
        if not code.is_active():
            raise APIException('Invalid code')
        
        # Generate token
        token = RefreshToken.for_user(request.user)

        # Invalidate code
        code.status = False
        code.save()

        payload = {
            'access': str(token.access_token),
            'refresh': str(token)
        }
        
        # Return token
        return Response(payload)