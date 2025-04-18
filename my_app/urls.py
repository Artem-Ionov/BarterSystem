from django.urls import path
from .views import ad_list, create_ad, delete_ad, update_ad, proposal_list, create_proposal, proposal_status, delete_proposal

urlpatterns = [
    path('', ad_list, name='ad_list'),
    path('<filter_param>', ad_list, name='ad_list_filter'),
    path('create/', create_ad, name='create_ad'),
    path('delete/<int:id>', delete_ad, name='delete_ad'),
    path('update/<int:id>', update_ad, name='update_ad'),
    path('proposal/', proposal_list, name='proposal_list'),
    path('proposal/create', create_proposal, name='create_proposal'),
    path('proposal/status/<int:id>', proposal_status, name='proposal_status'),
    path('proposal/delete/<int:id>', delete_proposal, name='delete_proposal'),
]