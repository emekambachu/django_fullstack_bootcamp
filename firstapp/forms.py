# import forms from django
from django import forms

# import validator from django.core
from django.core import validators

# create your own custom validator
# def check_for_z(value):
#     #if the first letter does not start with z
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class ContactForm(forms.Form):
    # name = forms.CharField(validators=[check_for_z])

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    verify_email = forms.EmailField(label='Enter your email again', widget=forms.TextInput(attrs={'class':'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    # hidden field for botcatcher
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # use this function to validate
    # add form field name in function
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        name = all_clean_data['name']

        # create validation statement
        if email != vmail:
             raise forms.ValidationError("MAKE SURE EMAILS MATCH")

        if len(name) < 3:
            raise forms.ValidationError("NAME NEEDS TO BE MORE THAN THREE CHARACTERS")


    # botcatcher function for validation
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BITCH")
    #     return botcatcher