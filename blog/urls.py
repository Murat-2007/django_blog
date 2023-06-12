from django.urls import path
from .views import post_list, post_delete, post_create, post_update, singers, post_detail, add_comment, add_or_remove_favorite, post_list_favorite_user, get_child_comment_form, new_add_comment

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post_delete/<slug>', post_delete, name='post_delete'),
    path('post_detail/<slug>', post_detail, name='post_detail'),
    path('post_create/', post_create, name='post_create'),
    path('post_update/<slug>', post_update, name='post_update'),
    path('add_comment/<slug>', add_comment, name='add_comment'),
    path('get_child_comment_form/', view=get_child_comment_form, name='get_child_comment_form'),
    path('new_add_comment/<int:pk>/<model_type>', new_add_comment, name='new_add_comment'),
    path('post_favorite_users/<slug>',post_list_favorite_user, name='post_list_favorite_user'),
    path('add_or_remove_favorite/<slug>', add_or_remove_favorite, name='add_or_remove_favorite'),
    path('singers/<int:sayi>/', singers),
]