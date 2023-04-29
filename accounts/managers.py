from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, firstname, lastname, phone, password=None):
        if not phone:
            raise ValueError("User Must Have a Phone")
        user = self.model(
            firstname=firstname,
            lastname=lastname,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, lastname, phone, password=None):
        user = self.create_user(
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
