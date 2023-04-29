import jdatetime
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from extensions.utils import create_profile_image_path

from .managers import UserManager


class User(AbstractBaseUser):
    firstname = models.CharField(max_length=100, verbose_name="نام")
    lastname = models.CharField(max_length=100, verbose_name="نام خانوادگی")
    phone = models.CharField(max_length=11, unique=True, verbose_name="شماره تلفن")
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name="ایمیل")
    image = models.ImageField(upload_to=create_profile_image_path, null=True, blank=True, verbose_name="تصویر")
    is_admin = models.BooleanField(default=True, verbose_name="مدیر")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ساخت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["firstname", "lastname"]

    objects = UserManager()

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def jalali_created_at(self):
        jalili_date = jdatetime.date.fromgregorian(date=self.created_at)
        return f"{jalili_date.year}/{jalili_date.month}/{jalili_date.day}"

    jalali_created_at.short_description = "عضویت"

    def jalali_updated_at(self):
        jalili_date = jdatetime.date.fromgregorian(date=self.updated_at)
        return f"{jalili_date.year}/{jalili_date.month}/{jalili_date.day}"

    jalali_updated_at.short_description = "ویرایش"

    def jalali_last_login(self):
        jalili_date = jdatetime.date.fromgregorian(date=self.last_login)
        return f"{jalili_date.year}/{jalili_date.month}/{jalili_date.day}"

    jalali_last_login.short_description = "آخرین ورود"
