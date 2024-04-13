from django.db import models

# Create your models here.

class UserWallet(models.Model):
    userId = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userId