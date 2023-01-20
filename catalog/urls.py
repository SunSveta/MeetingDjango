from django.urls import path
from catalog.views import v_home, v_contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', v_home),
    path('contacts/', v_contacts)
]