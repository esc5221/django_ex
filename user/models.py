from django.db import models

# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from seminar.models import Seminar


class CustomUserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일을 설정해주세요.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):

        # setdefault -> 딕셔너리에 key가 없을 경우 default로 값 설정
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # TODO
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('권한 설정이 잘못되었습니다.')

        # TODO
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    # TODO
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128, verbose_name='password')
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    last_login = models.DateTimeField(default=timezone.now)

    seminars = models.ManyToManyField(Seminar, through='seminar.UserSeminar')

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.email
