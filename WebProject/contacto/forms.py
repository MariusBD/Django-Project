from django import forms

class FormContacto(forms.Form):
    nombre = forms.CharField(label='Nombre',required=True)
    email = forms.CharField(label='Email',required=True)
    asunto = forms.CharField(label='Asunto',widget=forms.Textarea)
