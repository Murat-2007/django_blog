from django.urls import path
#from django.conf.urls import url
from .views import kullanici_takip_et_cikar, fallowed_or_fallowers_list, kullanici_modal_takip_et_cikar, kullanici_takip_et_cikar_for_post 

urlpatterns = [
    path('takiplesme_sistemi/', kullanici_takip_et_cikar, name='kullanici_takip_et_cikar'),
    path('post_fav_user_takip_et_cikar/', kullanici_takip_et_cikar_for_post, name='post_fav_user_takip_et_cikar'),
    path('modal_takip_et_cikar/', kullanici_modal_takip_et_cikar, name='modal_takip_et_cikar'),
    path('fallowed_or_fallowers_list/<fallow_type>', view=fallowed_or_fallowers_list, 
        name='fallowed_or_fallowers_list'),
]