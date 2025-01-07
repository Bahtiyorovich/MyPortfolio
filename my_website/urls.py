from django.urls import path
from .views import home, AboutView, CredentialsView

urlpatterns = [
    path('', home, name='home'),
    path('about_me/', AboutView.as_view(), name='about'),
    path('credentials/', CredentialsView.as_view(), name='credentials')
]