from django import forms
from .models import Contact
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ["name", "phone_number", "message"]

