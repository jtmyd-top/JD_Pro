from django import forms
from django.forms import widgets
import re
def validate_custom_format(value):
    # 定义允许的键名对应关系，pin 对应 wskey，pt_pin 对应 pt_key
    key_mapping = {
        'pin': 'wskey',
        'pt_pin': 'pt_key'
    }

    # 构建验证的正则表达式
    pattern = r'(pin|pt_pin)=.*?;(wskey|pt_key)=.*?;|(wskey|pt_key)=.*?;(pin|pt_pin)=.*?;$'

    if not re.match(pattern, value):
        raise forms.ValidationError(
            '输入格式必须为 pin=***;wskey=***; 或者 pt_key=***;pt_pin=***;'
        )
# 定义表单类
class UserloginForm(forms.Form):
    env = forms.CharField(
        required=True,
        max_length=1002,
        min_length=1,
        validators=[validate_custom_format],
        widget=forms.Textarea(attrs={
            'class': 'form-env',
            'placeholder': "请输入京东COOKIE或者WSKEY",
            
        }),
        error_messages={
            "max_length": "京东COOKIE或者WSKEY至多为1002位",
            "min_length": "京东COOKIE或者WSKEY最少为1位",
            "required": "京东COOKIE或者WSKEY不能为空",
        }
    )
    remark = forms.CharField(
        required=False,  # 设置为 False 表示该字段为可选
        max_length=1002,
        widget=forms.TextInput(attrs={
            'class': 'form-username',
            'disabled': 'disabled',
            'placeholder': "请输入备注/uuid,默认(为空)京东账户名"
        }),
        error_messages={
            "max_length": "备注/uuid,至多为1002位",
        }
    )
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['remark'].widget.attrs.update({'class': 'form-username', })	
class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=1002,widget=widgets.TextInput(attrs={'class': 'form-username', 'placeholder': "请输入京东账户名(pin)/备注/uuid"}), min_length=1,error_messages={
                                   "max_length": "京东账户名/pin/备注至多为1002位",
                                   "min_length": "京东账户名/pin/备注最少为1位",
                                   "required": "京东账户名/pin/备注不能为空",
                               })