from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('like/<int:post_id>', like, name='like'),
    path('singlepost/<int:post_id>', singlepost, name='singlepost'),
]