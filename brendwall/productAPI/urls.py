from django.contrib import admin
from django.urls import path
from .views import ProductAPIview
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'chats', ChatViewSet, basename='chat')

urlpatterns = [
    path('products/', ProductAPIview.as_view()),
]
