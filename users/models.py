from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    referral_code = models.CharField(max_length=20, blank=True, null=True)
    referred_by = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True)
    points = models.IntegerField(default=0)  # Track referral points
    timestamp = models.DateTimeField(auto_now_add=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Handle awarding points for referrals
        if self.referred_by:
            self.referred_by.points += 1  # Award point to referrer
            self.referred_by.save()
