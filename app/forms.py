from django import forms 

from django.core import validators

def validate_for_a(value):

    a = value.lower()
    if a[0]=='a':
        raise forms.ValidationError("NAME DOESNOT START WITH A ")


def length(value):

    if len(value) >5:
        raise forms.ValidationError("length exceeed")


class userform(forms.Form):

    name=forms.CharField(max_length=100,validators=[validate_for_a,validators.MinLengthValidator(5)])
    age=forms.IntegerField(validators=[validators.MinValueValidator(18  )])
    # email=forms.CharField(max_length=100)
    # reemail=forms.EmailField(max_length=100)
    # botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    # def clean(self):

    #     age  = self.cleaned_data['age']
        
    #     if age >28:
    #         raise forms.ValidationError("not suitable")
    # def clean_botcatcher(self):
    #     bot=self.cleaned_data['botcatcher']
    #     if len(bot)>0:
    #         raise forms.ValidationError('bot is catched')

    # def clean(self):
    #     e = self.cleaned_data['email']
    #     re = self.cleaned_data['reemail']

    #     if e != re:
    #         raise forms.ValidationError("not match")

