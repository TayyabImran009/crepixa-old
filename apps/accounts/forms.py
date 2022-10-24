from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext as _
from django_countries.fields import CountryField


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(),
    )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    def clean(self):
        cleaned_data = super().clean()
        error_messages = {
            'invalid_credentials': _('Invalid login credentials!'),
            'inactive': _('This account is inactive!'),
        }

        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:

            user = get_user_model().objects.filter(email__iexact=email).first()

            if not user or not user.check_password(password):
                raise forms.ValidationError(error_messages['invalid_credentials'])

            if not user.is_active:
                raise forms.ValidationError(error_messages['inactive'])

            return user, cleaned_data.get('remember_me')

        return None, None


class BaseSignupForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        user = get_user_model().objects.filter(email__iexact=email).first()
        if user:
            raise forms.ValidationError(_('There is a user with this email!'))

        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        self.instance.email = self.cleaned_data.get('email')
        password_validation.validate_password(password, self.instance)

        return password


class SignupForm(BaseSignupForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    country = CountryField(blank_label=_('Choose your country')).formfield(required=True, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('title', 'first_name', 'last_name', 'email', 'password', 'country', 'company_name')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])
        user.email_confirmation_token = user.generate_token()
        user.is_active = False

        if commit:
            user.save()

        return user


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()

    def set_token(self):
        user = get_user_model().objects.filter(email__iexact=self.cleaned_data['email']).first()

        if user:
            user.reset_password_token = user.generate_token()
            user.save()

        return user


class ConfirmTokenForm(forms.Form):
    token = forms.CharField()

    def clean_token(self):
        token = self.cleaned_data['token']
        if token == '':
            raise forms.ValidationError(_('Link is invalid!'))

        user = get_user_model().objects.filter(reset_password_token=self.cleaned_data['token']).first()

        if not user:
            raise forms.ValidationError(_('Link is invalid!'))

        return token


class ResetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_confirmation')

        if not password1 or not password2:
            raise forms.ValidationError('')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('Passwords don\'t match!'))

        password_validation.validate_password(password1)

        return self.cleaned_data

    def change_password(self, token: str):
        user = get_user_model().objects.filter(reset_password_token=token).first()

        if user:
            user.is_active = True
            user.reset_password_token = None
            user.set_password(self.cleaned_data['password'])
            user.save()

        return user


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(),
    )
    password_confirmation = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = get_user_model()
        fields = ('password', 'password_confirmation')

    def clean_password_confirmation(self):
        password = self.cleaned_data['password']
        password_confirmation = self.cleaned_data['password_confirmation']

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError(_('Passwords don\'t match!'))

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user


class BaseAccountForm(forms.ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        user = get_user_model().objects.filter(email__iexact=email).exclude(pk=self.instance.pk).first()
        if user:
            raise forms.ValidationError(_('There is a user with this email!'))

        return email


class AccountForm(BaseAccountForm):
    title = forms.CharField(widget=forms.RadioSelect)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    city = forms.CharField(required=False)
    zip_code = forms.CharField(required=False)
    company_name = forms.CharField(required=False)
    street_house_no = forms.CharField(required=False)
    country = CountryField(blank_label=_('Choose your country')).formfield(required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'email', 'city', 'country',
            'street_house_no', 'zip_code', 'title', 'company_name',
        )
