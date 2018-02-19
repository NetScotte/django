from django import forms
from user import models


# 用户登陆
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(widget=forms.PasswordInput, label='密码')


# 用户添加
class UserAdd(forms.Form):
    username = forms.CharField(label='用户名')
    password0 = forms.CharField(widget=forms.PasswordInput, label='密码')
    password1 = forms.CharField(widget=forms.PasswordInput, label='确认密码')
    label = forms.CharField(widget=forms.Textarea, label='个性签名')

    def is_valid(self):
        super(UserAdd, self).is_valid()
        password0 = self.data.get('password0')
        password1 = self.data.get('password1')

        if not password0 == password1:
            return False
        elif models.User.get_user(self.data.get('username')):
            return False
        else:
            return True

