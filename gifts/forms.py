from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(max_length=25, widget=forms.PasswordInput)


class AddUserForm(forms.ModelForm):
    password2 = forms.CharField(label='Potwierdź hasło', widget=forms.PasswordInput, max_length=20)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['password', 'first_name', 'last_name', 'email', 'password2']
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "Hasła się różnią",
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user