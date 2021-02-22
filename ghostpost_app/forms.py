from django import forms


class CreatePostForm(forms.Form):
    GHOSTPOST_CHOICES = (
        ('False', 'Boasts'),
        ('True', 'Roasts')
    )

    text = forms.CharField(max_length=100)
    is_roast = forms.ChoiceField(choices=GHOSTPOST_CHOICES)
    # good practice to start with default=0 for IntegerField()
