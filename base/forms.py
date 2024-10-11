from django import forms
from .models import Funcionarios


class LoginForm(forms.ModelForm):
    
    usuario = forms.Charfield(
        label = 'Usuário',
        max_length = 100,
        required = True,
        widget = forms.TextInput(), 
    )

    senha = forms.Charfield(
        label = 'Senha',
        max_length = 50,
        required = True,
        widget = forms.PasswordInput(), 
    )