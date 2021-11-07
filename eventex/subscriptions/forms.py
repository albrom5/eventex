from django import forms

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)
