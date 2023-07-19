from django import  forms
from .models import Ad,Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    category = forms.CharField(required=False)

COMMON_PASSWORDS = ['password', '123456', 'qwerty', 'letmein']
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Это имя уже занято другим пользователем.")
        if not username.replace('_', '').replace('-', '').isalnum():
            raise forms.ValidationError(
                "Недопустимое имя пользователя. Используйте только буквенно-цифровые символы, знаки подчеркивания и тире.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Эта почта уже привязана к другому аккаунту.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        return password1

    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        password1 = self.cleaned_data.get('password1')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")
        if password2.isdigit():
            raise forms.ValidationError("Пароль не может состоять только из цифр.")
        if password2.lower() == self.cleaned_data.get('username').lower():
            raise forms.ValidationError("Пароль слишком схож с именем пользователя.")
        if password2.lower() in COMMON_PASSWORDS:
            raise forms.ValidationError("Этот пароль слишком простой.")
        try:
            if len(password1) < 8:
                raise forms.ValidationError("Пароль не может быть короче 8 символов.")
        except:
            raise forms.ValidationError("Недопустимые символы в пароле")
        return password2
class AdPlacementForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone Number')
    location = forms.CharField(label='Location')

    class Meta:
        model = Ad
        fields = ['name', 'photo', 'description', 'price', 'category', 'email', 'phone', 'location']

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ['name', 'description', 'price', 'category', 'email', 'phone', 'location']
        missing_fields = []

        for field in required_fields:
            if not cleaned_data.get(field):
                missing_fields.append(field)

        if missing_fields:
            error_msg = "The following fields are required: {}".format(", ".join(missing_fields))
            self.add_error(None, error_msg)

        return cleaned_data