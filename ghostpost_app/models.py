from django.db import models


#
#     Boolean to tell whether it's a boast or a roast
#     CharField to put the content of the post in
#     IntegerField for up votes
#     IntegerField for down votes
#     DateTimeField for submission time
#

class Post(models.Model):
    roast_or_boast = models.BooleanField(default=False)
    text = models.CharField(max_length=100)
    # good practice to start with default=0 for IntegerField()
    boasts = models.IntegerField(default=0)
    roasts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # dunder method to make admin more readable
    def __str__(self):
        return self.text, self.boasts, self.roasts, self.created_at
