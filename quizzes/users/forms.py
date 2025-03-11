from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


# Форма для регистрации
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Удалить help_text для всех полей
        for field_name in self.fields:
            self.fields[field_name].help_text = None

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Этот email уже зарегистрирован.")
        return email


# Форма для редактирования профиля
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
