from .models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []

