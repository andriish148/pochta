from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введіть email'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Додаємо CSS класи для кращого вигляду
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введіть логін'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введіть пароль'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Підтвердіть пароль'})