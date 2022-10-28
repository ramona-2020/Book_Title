from django import forms

from Book_Talk.web.models import User

PASSWORD_CONFIRMATION_ERROR_MESSAGE = 'Password and confirmed password does not match'


class UserBaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'box'

            if _ == 'review':
                field.widget.attrs['rows'] = 0
                field.widget.attrs['cols'] = 0

    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_passwords = cleaned_data.get('confirm_password')

        if password != confirm_passwords:
            raise forms.ValidationError(PASSWORD_CONFIRMATION_ERROR_MESSAGE)

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }


class UserRegisterForm(UserBaseForm):
    pass

