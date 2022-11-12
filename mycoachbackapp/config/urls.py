from django.contrib import admin
from django.urls import path, include

app_name = "config"


root_urlpatterns = [
    path("api_coafro/", include("apis.api_coafro.urls", namespace="api_coafro")),
    path("admin/", admin.site.urls, name="admin"),  # Admin
    path("cd/", include("coach_dashboard.urls", namespace="cd")),  # Back Office

]

urlpatterns = [
    path("backend/", include(root_urlpatterns)),
    path("api/v1/", include('djoser.urls')),
    path("api/v1/", include('djoser.urls.authtoken')),
]