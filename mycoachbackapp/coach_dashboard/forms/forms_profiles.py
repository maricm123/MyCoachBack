from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from profiles.models.coach import Coach
from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.db.models import Q

User = get_user_model()

class UserCacheMixin:
	user_cache = None

# SIGN UP FORMS
class CoachSignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

	def clean_email(self):
		email = self.cleaned_data['email']

		user = User.objects.filter(email__iexact=email).exists()
		if user:
			raise ValidationError(_('You can not use this email address.'))

		return email


# LOGIN FORMS
class EmailOrUsernameForm(UserCacheMixin, forms.Form):
	email_or_username = forms.CharField(label=_('Email or Username'))

	def clean_email_or_username(self):
		email_or_username = self.cleaned_data['email_or_username']

		user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
		if not user:
			raise ValidationError(_('You entered an invalid email address or username.'))

		# if not user.is_coach:
		# 	raise ValidationError(_("You are not coach"))

		if not user.is_active:
			raise ValidationError(_('This account is not active.'))

		self.user_cache = user

		return email_or_username


class LoginForm(UserCacheMixin, forms.Form):
	password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# if settings.USE_REMEMBER_ME:
		#     self.fields['remember_me'] = forms.BooleanField(label=_('Remember me'), required=False)

	def clean_password(self):
		password = self.cleaned_data['password']

		if not self.user_cache:
			return password

		if not self.user_cache.check_password(password):
			raise ValidationError(_('You entered an invalid password.'))

		return password


class CoachLoginForm(LoginForm, EmailOrUsernameForm):
	pass


class CoachProfilePageForm(forms.ModelForm):
	model = Coach
	fields = ('user', 'biography')

	# widgets for fileds