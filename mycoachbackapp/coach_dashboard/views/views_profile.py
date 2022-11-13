from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, View, FormView
from profiles.models.coach import Coach
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.decorators import method_decorator
from ..forms.forms_profiles import CoachSignUpForm, CoachLoginForm
from django.conf import settings
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME, logout
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse

User = get_user_model()

class GuestOnlyView(View):
	def dispatch(self, request, *args, **kwargs):
		# Redirect to the index page if the user already authenticated
		if request.user.is_authenticated:
			return redirect(settings.LOGIN_REDIRECT_URL)

		return super().dispatch(request, *args, **kwargs)


class CoachSignUp(GuestOnlyView, FormView):
	template_name = 'profiles/coach_signup.html'
	form_class = CoachSignUpForm

	def form_valid(self, form):
		request = self.request
		user = form.save(commit=False)

		coach = Coach

		# if settings.DISABLE_USERNAME:
		# 	# Set a temporary username
		# 	user.username = get_random_string()
		# else:
		# 	user.username = form.cleaned_data['username']

		# if settings.ENABLE_USER_ACTIVATION:
		# 	user.is_active = False

		# # Create a user record
		# user.is_coach = True
		user.save()
		user.is_coach = True
		Coach.objects.create(user=user)

		# # Change the username to the "user_ID" form
		# if settings.DISABLE_USERNAME:
		# 	user.username = f'user_{user.id}'
		# 	user.save()

		# if settings.ENABLE_USER_ACTIVATION:
		# 	code = get_random_string(20)

		# 	act = Activation()
		# 	act.code = code
		# 	act.user = user
		# 	act.save()

		# 	send_activation_email(request, user.email, code)

		# 	messages.success(
		# 		request, _('You are signed up. To activate the account, follow the link sent to the mail.'))
		# else:
		# 	raw_password = form.cleaned_data['password1']

		# 	user = authenticate(username=user.username, password=raw_password)
		# 	login(request, user)

		# 	messages.success(request, _('You are successfully signed up!'))

		return redirect('cd:coachlogin')

class CoachLogin(GuestOnlyView, FormView):
	template_name = "profiles/coach_login.html"

	@staticmethod
	def get_form_class(**kwargs):
		return CoachLoginForm

	@method_decorator(sensitive_post_parameters('password'))
	@method_decorator(csrf_protect)
	@method_decorator(never_cache)
	def dispatch(self, request, *args, **kwargs):
		# Sets a test cookie to make sure the user has cookies enabled
		request.session.set_test_cookie()

		return super().dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		request = self.request

		# If the test cookie worked, go ahead and delete it since its no longer needed
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()

		# The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
		# the SESSION_COOKIE_AGE settings' option.
		# if settings.USE_REMEMBER_ME:
		#     if not form.cleaned_data['remember_me']:
		#         request.session.set_expiry(0)
		login(request, form.user_cache)
		# redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME))
		# url_is_safe = is_safe_url(redirect_to, allowed_hosts=request.get_host(), require_https=request.is_secure())

		# if url_is_safe:
		#     return redirect(redirect_to)

		return redirect(settings.LOGIN_REDIRECT_URL)


class LogoutView(View):
	def get(self, request):
		user = request.user  # used for logging purpose only
		logout(request)
		return HttpResponseRedirect(reverse(settings.LOGIN_URL))
	