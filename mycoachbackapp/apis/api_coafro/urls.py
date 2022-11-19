from django.conf import settings
from django.urls import include, path
from .views import views_profiles
from . import views
from rest_framework.routers import DefaultRouter
from .views.views_profiles import ClientSignUpView, CoachSignUpView, CoachLoginView
from .views.views_program import ProgramView, CoachProgramView

app_name = "api_coafro"

router = DefaultRouter()
router.register('programs', ProgramView, basename='programs')
router.register('coach_programs', CoachProgramView, basename='coach_programs')

urlpatterns = [
    # profiles
    path("clientsignup/", views.views_profiles.ClientSignUpView.as_view(), name = "clientsignup"),
    path("coachsignup/", views.views_profiles.CoachSignUpView.as_view(), name = "coachsignup"),
    path("coachlogin/", views.views_profiles.CoachLoginView.as_view(), name = "coachlogin"),
    path("clientlogin/", views.views_profiles.CoachLoginView.as_view(), name = "clientlogin"),
    
    # program
    path('', include(router.urls)),



]