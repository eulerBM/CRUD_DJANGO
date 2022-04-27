from django import forms
from app1.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

    