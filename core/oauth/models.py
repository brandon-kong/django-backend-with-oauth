import secrets
from django.db import models
from django.contrib.auth import get_user_model

from django.conf import settings
from base64 import urlsafe_b64encode

from django.utils import timezone

def generate_client_id():
    n_bytes = settings.COREAPP_CLIENTID_N_BYTES or 16
    # Generate a random client_id with n bytes
    id = secrets.token_hex(n_bytes)
    url_save = urlsafe_b64encode(id.encode()).decode()
    return url_save

def generate_authorization_code():
    n_bytes = 16
    # Generate a random authorization code with n bytes
    code = secrets.token_hex(n_bytes)
    url_save = urlsafe_b64encode(code.encode()).decode()
    return url_save

class ApplicationClient(models.Model):
    name = models.CharField(max_length=255)

    authorized_origins = models.TextField()
    authorized_redirect_uris = models.TextField()

    client_id = models.CharField(max_length=255, unique=True, default=generate_client_id)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.client_id
    
class ClientSecret(models.Model):
    client = models.ForeignKey(ApplicationClient, on_delete=models.CASCADE)
    secret = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.secret
    
class AuthorizationCode(models.Model):
    client = models.ForeignKey(ApplicationClient, on_delete=models.CASCADE)
    code = models.CharField(max_length=255, unique=True, default=generate_authorization_code)

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
    def is_active(self):
        return self.status == True and self.created_at > timezone.now() - timezone.timedelta(minutes=10)
    
