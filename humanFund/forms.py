from django import forms
from . import static

class RegisForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Username'}))
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={'class' : 'humanInput', 'placeholder' : 'Password'}))
    fName = forms.CharField(label='First Name', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'First Name'}))
    mName = forms.CharField(label='Middle Name', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Middle Name'}))
    lName = forms.CharField(label='Last Name', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Last Name'}))
    gender = forms.CharField(label='Gender', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Gender'}))
    address = forms.CharField(label='Street Address', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Street Address'}))
    city = forms.CharField(label='City', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'City'}))
    email = forms.CharField(label='Email Address', max_length=20, widget=forms.EmailInput(attrs={'class' : 'humanInput', 'placeholder' : 'Email Address'}))
    cellPhone = forms.CharField(label='Cell Phone Number', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Cell Phone Number'}))
    country = forms.CharField(label='Country', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Country'}))
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'class' : 'humanInput', 'placeholder' : 'Date of Birth'}))

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Username'}))
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput(attrs={'class' : 'humanInput', 'placeholder' : 'Password'}))

class Portal(forms.Form):
    office = forms.CharField(label='Office', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Office'}))
    officer = forms.CharField(label='Officer', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Officer'}))
    org = forms.CharField(label='Organization', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Organization'}))
    orgMember = forms.CharField(label='Organization Member', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Organization Member'}))
    subscriber = forms.CharField(label='Subscriber', max_length=20, widget=forms.TextInput(attrs={'class' : 'humanInput', 'placeholder' : 'Subscriber'}))
