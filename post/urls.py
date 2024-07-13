from django.urls import path

from . import api


urlpatterns = [
    path('', api.post_list, name='post_list'), # list of posts
    path('<uuid:pk>/like/', api.post_like, name='post_like'), # like a post
    path('profile/<uuid:id>/', api.post_list_profile, name='post_list_profile'), # posts of a specific user
    path('create/', api.post_create, name='post_create'), # create a post
]