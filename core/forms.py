from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "contact-form-input",
                    "placeholder": "Votre nom complet"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "contact-form-input",
                    "placeholder": "Votre adresse e-mail"
                }
            ),

            "subject": forms.TextInput(
                attrs={
                    "class": "contact-form-input",
                    "placeholder": "Objet de votre message"
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "contact-form-input contact-form-textarea",
                    "placeholder": "Votre message...",
                    "rows": 6
                }
            ),
        }