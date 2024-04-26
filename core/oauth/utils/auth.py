from django.conf import settings

class OAuth2:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_authorization_url(self):
        pass  # Implement this

    def exchange_code_for_token(self, code):
        pass  # Implement this

    def get_user_info(self, access_token):
        pass  # Implement this