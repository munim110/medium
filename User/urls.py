from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('', signin, name='signin'),
    path('error/', error, name='error'),
    path('signout/', signout, name='signout'),
    path('profile/<slug:username>', profile, name='profile'),
]