# _*_ coding: utf-8 _*_

from django import forms
from django.contrib.auth.models import Group, Permission
from .models import UserProfile
from django.contrib.auth import authenticate,login
from django.forms import widgets
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, UserChangeForm


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=12, min_length=4)
    password = forms.CharField(required=True, max_length=12, min_length=4)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username','name_cn','password','email','phone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'name_cn': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': ' form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),

        }

    def __init__(self,*args,**kwargs):
        super(UserProfileForm, self).__init__(*args,**kwargs)
        self.fields['username'].label = u'账 号'
        self.fields['username'].error_messages = {'required': u'请输入账号'}
        self.fields['name_cn'].label = u'账 号'
        self.fields['name_cn'].error_messages = {'required': u'请输入中文名字'}
        self.fields['password'].label = u'密 码'
        self.fields['password'].error_messages={'required': u'请输入密码'}
        self.fields['email'].label = u'邮 箱'
        self.fields['email'].error_messages = {'required': u'请输入邮箱', 'invalid': u'请输入有效邮箱'}
        self.fields['phone'].label = u'电话'
        self.fields['phone'].error_messages={'required': u'请输入电话号码'}


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6  :
            raise forms.ValidationError(u'密码必须大于6位/密码为空')
        return password


class UserPwdForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['password']

class PowerForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = "__all__"

class PowerUpdateForm(forms.ModelForm):
    class Meta:
        model = Permission
        fields = ['name','codename']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"



class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name_cn','phone','email']

