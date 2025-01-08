from django.urls import path
from .views import home, AboutView, CredentialsView, WorksView, WorkDetailView

urlpatterns = [
    path('', home, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('credentials/', CredentialsView.as_view(), name='credentials'),
    path('works/', WorksView.as_view(), name='works'),
    path('work/<slug:slug>/', WorkDetailView.as_view(), name='work_detail'),
]