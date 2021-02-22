from django import forms


class CreatePostForm(forms.Form):
    text = forms.CharField(max_length=100)
    # good practice to start with default=0 for IntegerField()
    boast = forms.IntegerField()
    roast = forms.IntegerField()
