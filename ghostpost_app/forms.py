from django import forms


class CreatePostForm(forms.Form):
    text = forms.CharField(max_length=100)
    is_roast = forms.ChoiceField(choices=[[0, 'Roast'], [1, 'Boast']])
    # good practice to start with default=0 for IntegerField()
    boast = forms.IntegerField()
    roast = forms.IntegerField()
