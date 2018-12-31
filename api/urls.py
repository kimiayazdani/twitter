from django.urls import path
from .views import version1 as version1View
from .views import version2 as version2View

urlpatterns = [
    path('v1/<str:index>' , version1View.Index.as_view(), name="version1"),
    path('v2/<str:index>' , version2View.Index.as_view(), name="version2")
]