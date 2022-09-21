from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('like/<int:post_id>', like, name='like'),
    path('singlepost/<int:post_id>', singlepost, name='singlepost'),
    path('editpost/<int:post_id>', editPost, name='editpost'),
    path('editcomment/<int:post_id>/<int:comment_id>', editComment, name='editcomment'),
]