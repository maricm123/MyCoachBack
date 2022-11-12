from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, View, FormView
from profiles.models.coach import Coach
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.decorators import method_decorator
from ..forms.forms_profiles import CoachSignUpForm, CoachLoginForm
from django.conf import settings
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import get_user_model





class CoachDashboard(ListView):
    login_required = True
    model = Coach
    context_object_name = 'coach'
    template_name='programs/dashboard.html'

    def get_queryset(self):
        pass