from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from users_control.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class RegisterForm(forms.Form):
    username = forms.CharField(label='Alias', required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : '',
                                    'id' : 'username',
                                    'placeholder' : 'Username'
                                }))
    email = forms.EmailField(label='Correo electrónico', required=True,
                            widget=forms.EmailInput(attrs={
                                'class' : '',
                                'id' : 'username',
                                'placeholder' : 'example@gmail.com'
        }))
    
    password = forms.CharField(label='Password', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class' : ''
                                }))
    
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email

    def save(self):
        return CustomUser.objects.create_user(
            self.cleaned_data.get('email'),
            password = self.cleaned_data.get('password'),
            username = self.cleaned_data.get('username'),
            
        )
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username', required=True,
                               widget=forms.EmailInput(attrs={
                                'class' : '',
                                'id' : 'email_username',
                                'placeholder' : 'example@gmail.com'
        })
                                )
    
    password = forms.CharField(label='Password', required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class' : ''
                                }))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
