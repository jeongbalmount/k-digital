from django import forms


def max_length_10_validator(value):
    if len(value) > 10:
        raise forms.ValidationError('10글자 이하로 입력해주세요')


class PostForm(forms.Form):
    inputText = forms.CharField(validators=[max_length_10_validator])


