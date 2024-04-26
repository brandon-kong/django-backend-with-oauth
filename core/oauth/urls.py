from django.urls import path

from .views import (
    OAuth2AuthorizeView,
    OAuth2TokenView,
)

urlpatterns = [
    path('authorize/', OAuth2AuthorizeView.as_view(), name='authorize'),
    path('token/', OAuth2TokenView.as_view(), name='token'),
]