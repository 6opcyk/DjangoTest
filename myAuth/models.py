from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, data):
        with open("log.txt","w") as log:
            log.write(str(data))
        account = self.model(email = self.normalize_email(data["email"]), 
                             last_name = data["last_name"],
                             first_name = data["first_name"])
        account.set_password(data["password"])
        account.save()
        return account

    def create_superuser(self, data):
        account = self.create_user(data)
        account.is_admin = True
        account.save()

        return account

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    eth_token = models.CharField(max_length = 120, default = "None")
    eth_adress = models.CharField(max_length = 120, default = "None")

    USERNAME_FIELD = 'email'
    
    objects = AccountManager()

