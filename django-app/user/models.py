from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length = 20)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
