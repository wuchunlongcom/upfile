from django import forms
from .models import Course


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ['id', 'image']
