# portfolio/forms.py
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'required': True}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5, 'required': True}),
        }