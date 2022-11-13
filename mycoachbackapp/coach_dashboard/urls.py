from django.urls import path
from .views.views_profile import CoachSignUp, CoachLogin, LogoutView
from .views.views_program import CoachDashboard

app_name = "core"

urlpatterns = [
    path("coach", view=CoachDashboard.as_view(), name="coach"),
    path("coachsignup", view=CoachSignUp.as_view(), name="coachsignup"),
    path("coachlogin", view=CoachLogin.as_view(), name="coachlogin"),
    path("logout", LogoutView.as_view(), name='logout'),

]