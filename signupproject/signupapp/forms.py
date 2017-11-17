#import form library
from django import forms

#Create class and say it uses Form template from forms library
class SignupForm(forms.Form):
    
    #create fields
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email", max_length=100)