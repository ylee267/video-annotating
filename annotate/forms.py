from django import forms
from annotate.models import Annotation


class UserForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ['nickname', 'email']


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        field = ['nickname', 'email', 'video', 'time', 'comment', 'comment_type']
