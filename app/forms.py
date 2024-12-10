from django import forms  
from django .contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField, PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import Customer


class CustomerRegissterationForm(UserCreationForm):
    password1 = forms.CharField(label='password',widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label=' Confirm password (again)',widget=forms.
    PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True,widget=forms.
    EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model  = User
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}
        
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=("password") ,strip=False ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    
    
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Old Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'autofocus': True,
            'class': 'form-control'  # Corrected 'form-cantrol' to 'form-control'
        })
    )
    
    new_password1 = forms.CharField(  # Changed to new_password1 as required by PasswordChangeForm
        label=('New Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'autofocus': True,
            'class': 'form-control'  # Corrected 'form-cantrol' to 'form-control'
        }),
        help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(  # Added new_password2 for confirmation
        label=('Confirm New Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control'
        })
    )
    
class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=("Email"), max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'autofocus': True,
            'class': 'form-control'  # Corrected 'form-cantrol' to 'form-control'
        })
    ) 
    
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control'  # Corrected 'form-cantrol' to 'form-control'
        }),
        help_text=password_validation.password_validators_help_text_html())
    
    new_password2 = forms.CharField(
        label=(" Confirm New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'confirm New Password',
            'class': 'form-control'  # Corrected 'form-cantrol' to 'form-control'
        }),
    )
    
from django import forms
from .models import Customer  # Ensure you import your Customer model

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }
