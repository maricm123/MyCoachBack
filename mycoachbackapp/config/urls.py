from django.contrib import admin
from django.urls import path, include
from django.conf import settings


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



if settings.DEBUG:
    from rest_framework import urls as rest_urls
    # Allow rest_framework login/logout views to test rest APIs
    urlpatterns += [path("", include(rest_urls, namespace="rest_framework"))]