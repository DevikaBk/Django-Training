from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields=('username','email','password1','password2')
 
class PostForm(forms.Form):
    title=forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
