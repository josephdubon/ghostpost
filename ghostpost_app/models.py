from django.db import models


class Post(models.Model):
    text = models.CharField(max_length=100)
    # good practice to start with default=0 for IntegerField()
    boast = models.IntegerField(default=0)
    roast = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # dunder method to make admin more readable
    def __str__(self):
        return self.text, self.boast, self.roast, self.created_at
