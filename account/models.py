from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAccount(AbstractUser):
    phone = models.IntegerField(unique=True, blank=True, null=True)
    balance = models.DecimalField(max_digits=12,decimal_places=2, default=0)
    nid = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='account/images/')
    address = models.TextField()


    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_accounts",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_accounts",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

