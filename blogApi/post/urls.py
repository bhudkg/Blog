from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'home', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('index/', your_view, name='your_view'),

    
]
