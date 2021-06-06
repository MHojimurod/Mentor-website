from django import forms
from .models import *

class NewsForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'