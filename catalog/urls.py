from django.urls import path
from catalog.views import v_home, v_contacts
from catalog.apps import CatalogConfig
from catalog.views import prod_card

app_name = CatalogConfig.name

urlpatterns = [
    path('', v_home, name='home'),
    path('contacts/', v_contacts, name='contacts'),
    path('prod_card/', prod_card, name='prod_card')
]