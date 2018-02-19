from django import forms


class LiuyanForm(forms.Form):
    title = forms.CharField(label='标题')
    content = forms.CharField(widget=forms.Textarea, label='内容')

    # 浏览器已有验证，此处不需验证是否为空
    # def is_valid(self):
    #     super(LiuyanForm, self).is_valid()
    #     if self.data.get('title') and self.data.get('content'):
    #         return True
    #     else:
    #         return False
