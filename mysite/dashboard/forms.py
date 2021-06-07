from django import forms
from mentor.models import Trainers,Events,Newsletter,User
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainers()
        fields = '__all__'

class NewsForm(forms.ModelForm):
    class Meta:
        model = Newsletter()
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User()
        fields = '__all__'