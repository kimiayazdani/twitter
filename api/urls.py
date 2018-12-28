from django.urls import path
from . import views


urlpatterns = [
    path('v1' , views.v1_index, name="version1"),
    path('v2' , views.v2_index, name="version2")
]