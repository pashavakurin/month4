from django import forms


class CreatePostForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(min_length=3, max_length=64)
    description = forms.CharField(widget=forms.Textarea())
    cost = forms.IntegerField(min_value=0)
    name_of_board = forms.CharField()
    size = forms.IntegerField(min_value=1)