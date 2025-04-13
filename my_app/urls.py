from django.urls import path
from .views import ad_list, create_ad, delete_ad, update_ad

urlpatterns = [
    path('', ad_list, name='ad_list'),
    path('create/', create_ad, name='create_ad'),
    path('delete/<int:id>', delete_ad, name='delete_ad'),
    path('update/<int:id>', update_ad, name='update_ad'),
]