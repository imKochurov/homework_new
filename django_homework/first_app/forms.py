from django import forms
from first_app.models import CallOrder, Notes

class CallOrderForm(forms.ModelForm):
    class Meta:
        model = CallOrder
        fields = ['user_name', 'user_surname', 'phone']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text', 'reminders', 'category']