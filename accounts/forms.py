from django import forms
from django.contrib.auth.models import User
from accounts.models import Profile
from django.utils.translation import ugettext_lazy as _



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [ 'password', 'username', 'first_name','last_name','email','confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
   	    user = super(RegisterForm, self).save(commit=False)
   	    user.set_password(self.cleaned_data["password"])
   	    if commit:
             user.save()
   	    return user

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['address','collegeid']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['address'].required = True
        self.fields['collegeid'].required = True
        