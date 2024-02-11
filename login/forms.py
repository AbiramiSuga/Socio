from django import forms
from django.forms import ModelForm
from .models import user


class registerForm(forms.ModelForm):
    error_css_class='error-field'
    required_css_class = 'required-field'
    u_name=forms.CharField(label="Name",widget=forms.TextInput(attrs={"class":"myfieldclass"})) #placeholder is for the text to be displayed in the input field
    u_mailid=forms.CharField(label="Mail id",widget=forms.TextInput(attrs={"class":"myfieldclass"}))
    pswd=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={"class":"myfieldclass"}))
    hobby=forms.CharField(label="Hobby",widget=forms.TextInput(attrs={"class":"myfieldclass"}))
    address=forms.CharField(label="Address",widget=forms.TextInput(attrs={"class":"myfieldclass"}))
    profession=forms.CharField(label="Profession",widget=forms.TextInput(attrs={"class":"myfieldclass"}))
    dob=forms.DateField(label="Date of Birth",widget=forms.DateInput(attrs={"class":"myfieldclass"}))
    education=forms.CharField(label="Education",widget=forms.TextInput(attrs={"class":"myfieldclass"}))
    phone_no=forms.CharField(label="Phone number",widget=forms.TextInput(attrs={"class":"myfieldclass"}))
    pic=forms.ImageField(label="Profile picture",widget=forms.FileInput(attrs={"class":"myfieldclass"}))

    class Meta:
        model=user
        fields=("u_name","u_mailid","pswd","hobby","address","profession","dob","education","phone_no","pic")
        

       



         # fields=("Name","Mail id","Password","Hobby","Address","Profession","Date of Birth","Education","Phone number","Profile pic")