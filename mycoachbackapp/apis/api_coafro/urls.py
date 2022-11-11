from django.conf import settings
from django.urls import include, path
from .views import views_profiles
from . import views
from rest_framework.routers import DefaultRouter
from .views.views_profiles import ClientSignUpView, CoachSignUpView
from .views.views_program import ProgramView

app_name = "api_coafro"

router = DefaultRouter()
router.register('programs', ProgramView, basename='programs')

urlpatterns = [
    # profiles
    path("clientsignup/", views.views_profiles.ClientSignUpView.as_view(), name = "clientsignup"),
    path("coachsignup/", views.views_profiles.CoachSignUpView.as_view(), name = "coachsignup"),

    # program
    # path("programs/", ProgramView.as_view(), name = "programs"),

    path('', include(router.urls)),



]