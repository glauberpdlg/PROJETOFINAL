from django import forms 
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'endereco',
            'telefone',
            'email'
        ]

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu nome"}),
            "endereco": forms.TextInput(attrs={"class": "form-control","placeholder": "Digite seu endereço"}),
            "telefone": forms.TextInput(attrs={"class": "form-control","placeholder": "(XX) XXXX-XXXX"}), # Exemplo de placeholder para Telefone
            "email": forms.EmailInput(attrs={"class": "form-control","placeholder": "email@example.com"}), # Usando EmailInput
            "data_cadastro": forms.DateInput(attrs={"class": "form-control","placeholder": "DD/MM/AAAA", 'type': 'date'}), # Usando DateInput e type='date'
        }