from django import forms
from mentor.models import Trainers,Events,Newsletter,User,Faculty,Course
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

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events()
        fields = '__all__'

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty()
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course()
        fields = '__all__'