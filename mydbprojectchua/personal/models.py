from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# For Practical
class Dvd(models.Model):
    dvd_id              = models.AutoField(primary_key=True)
    genre               = models.CharField(max_length=60, blank=True)
    title               = models.CharField(max_length=60, blank=True)
    release_year        = models.CharField(max_length=4, blank=True)

    class meta:
        db_table = 'tblDvd'




        

class RegUser(models.Model):
    user_id             = models.AutoField(primary_key=True)
    email               = models.EmailField(unique=True, blank=True)
    username            = models.CharField(max_length=60, unique=True, blank=True)
    password            = models.CharField(max_length=200, blank=True)

    class meta:
        db_table = 'tbluser'

class Post(models.Model):


    POST_STATUS_CHOICES =[
        ('PENDING', 'PENDING'),
        ('APPROVED','APPROVED'),
    ]
    postPK               = models.AutoField(primary_key=True)
    post_id              = models.CharField(max_length=4, blank=True)
    id                   = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title           = models.CharField(max_length=60, blank=True)
    post_content         = models.TextField(blank=True)
    post_status          = models.CharField(max_length=10, choices=POST_STATUS_CHOICES, default='PENDING', blank=True)

    class meta:
        db_table = 'tblpost'



# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError("Users must have an email address")
#         if not username:
#             raise ValueError("Users must have an username")
        
#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class Account(AbstractBaseUser):
#     email                   = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username                = models.CharField(max_length=30, unique=True)
#     date_joined             = models.DateField(verbose_name='date joined', auto_now_add=True)
#     last_login              = models.DateField(verbose_name='last login', auto_now=True)
#     is_admin                = models.BooleanField(default=False)
#     is_active               = models.BooleanField(default=True)
#     is_staff                = models.BooleanField(default=False)
#     is_superuser            = models.BooleanField(default=False)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username',]

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True

