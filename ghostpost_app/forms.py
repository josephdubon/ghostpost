from django import forms


class CreatePostForm(forms.Form):
    GHOSTPOST_CHOICES = (
        ('True', 'Yes, Roast'),
        ('False', 'No, A Boast!'),
    )

    text = forms.CharField(max_length=100)
    is_roast = forms.ChoiceField(choices=GHOSTPOST_CHOICES)
