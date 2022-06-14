from django import forms
from myform.models import Subscribe

class SubscribeForm(forms.ModelForm):
    email_address =forms.CharField(required=True,widget=forms.EmailInput(attrs={'placeholder':'Email address'}))
    first_name =forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    address = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Address'}))
    class Meta:
        model =Subscribe
        fields =['email_address','first_name','last_name','address']