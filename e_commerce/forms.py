from django import forms
from django.forms.fields import CharField

class ContactForm(forms.Form):
    nome_completo = forms.CharField(
        error_messages={"required":"Obrigatório o preenchimento do nome"},
        widget = forms.TextInput(
            attrs = {
                "class":"form-control",
                "placeholder":"Seu nome completo"
            }
        )
    )
    email = forms.EmailField(
        error_messages={"invalid":"Digite um e-mail válido!"},
        widget = forms.EmailInput(
        attrs = {
            "class":"form-control",
            "placeholder":"Seu e-mail"
        }
    ))
    Mensagem = forms.CharField(
        error_messages={"required":"O campo de mensagem é obrigatório..."},
        widget = forms.Textarea(
        attrs = {
            "class":"form-control",
            "placeholder":"Sua mensagem aqui..."
        }
    ))
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not "gmail.com" in email:
            raise forms.ValidationError("O e-mail deve ser do gmail.com")
        return email