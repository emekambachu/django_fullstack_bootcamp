from django import forms
from secondapp.models import User

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'