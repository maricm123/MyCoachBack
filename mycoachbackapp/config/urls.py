from django.contrib import admin
from django.urls import path, include

app_name = "config"


root_urlpatterns = [
    # path("api_coafro/", include("apis.api_coafro.urls", namespace="api_coafro")),
    path("admin/", admin.site.urls, name="admin"),  # Admin

]

urlpatterns = [
    path("backend/", include(root_urlpatterns)),
]