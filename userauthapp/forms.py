from django import forms
from django.contrib.auth.models import User
from . models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    # use this function to add classes to all form fields
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')

    # use this function to add classes to all form fields
    def __init__(self, *args, **kwargs):
        super(UserProfileInfoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'