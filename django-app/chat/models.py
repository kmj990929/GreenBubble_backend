
from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length=20)
    receiver = models.CharField(max_length=20)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} to {}'.format(self.sender, self.receiver)
