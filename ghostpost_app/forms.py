from django import forms


class CreatePostForm(forms.Form):
    GHOSTPOST_CHOICES = (
        ('1', 'boasts'),
        ('2', 'roasts')
    )

    text = forms.CharField(max_length=100)
    is_roast = forms.ChoiceField(choices=GHOSTPOST_CHOICES)
    # good practice to start with default=0 for IntegerField()
    boasts = forms.IntegerField()
    roasts = forms.IntegerField()
