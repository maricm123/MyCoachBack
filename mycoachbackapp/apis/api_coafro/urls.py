from django.conf import settings
from django.urls import include, path
from .views import views_profiles
from . import views
from rest_framework.routers import DefaultRouter
from .views.views_profiles import ClientSignUpView, CoachSignUpView, CoachLoginView, ClientLoginView
from .views.views_program import ProgramView, CoachProgramView, delete_program, ProgramDetail, CoachProgramDetail, CategoryView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "api_coafro"

# router = DefaultRouter()
# router.register('programs', ProgramView.as_view(), basename='programs')
# router.register('coach_programs', CoachProgramView, basename='coach_programs')
# router.register('delete_program/<int:program_id>', delete_program, basename='delete_program')

urlpatterns = [
    # program
    # path('', include(router.urls)),
    path('delete_program/<int:program_id>/', delete_program, name="delete_program"),
    path('programs/', views.views_program.ProgramView.as_view(), name="programs"),
    path('coach_programs/', views.views_program.CoachProgramView.as_view(), name="coach_programs"),
    path('programs/<id>', ProgramDetail.as_view(), name="program"),
    path('coach_programs/<id>', CoachProgramDetail.as_view(), name="coach_program"),

    # category
    path('category/', views.views_program.CategoryView.as_view(), name="category"),


    # profiles
    path("clientsignup/", views.views_profiles.ClientSignUpView.as_view(), name = "clientsignup"),
    path("coachsignup/", views.views_profiles.CoachSignUpView.as_view(), name = "coachsignup"),
    # simple jwt view urls
    path("coachlogin/", views.views_profiles.CoachLoginView.as_view(), name="coachlogin"),
    path("clientlogin/", views.views_profiles.ClientLoginView.as_view(), name="coachlogin"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),



]