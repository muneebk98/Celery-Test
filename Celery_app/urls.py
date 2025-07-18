from django.urls import path
from .views import github_webhook

urlpatterns = [
    path('webhook/github/', github_webhook),
]
