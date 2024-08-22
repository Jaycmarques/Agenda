from django import forms
from accounts.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        first_name = cleaned_data.get('first_name')

        # Adicionando erros se o nome for igual a um valor específico
        if first_name == 'Invalid':
            self.add_error(
                'first_name',
                'Nome inválido'
            )

        return cleaned_data
