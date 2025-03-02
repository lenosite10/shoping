from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManeger(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('لطفا ایمیل خود را وارد کنید')
        if not username:
            raise ValueError('نام کاربری باید وارد شود')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    
    
class Accounts(AbstractBaseUser):
    class Meta:
        verbose_name = 'پنل کاربری مدریت'
        verbose_name_plural = 'پنل کاربری مدیریت'
    first_name = models.CharField(max_length=50,verbose_name='نام')
    last_name = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    username = models.CharField(max_length=50,unique=True,verbose_name='نام کاربری')
    email = models.CharField(max_length=100,unique=True,verbose_name='ایمیل')
    phone_number = models.CharField(max_length=11,unique=True,null=True,verbose_name='شماره تماس')
    
    #requierd
    date_join = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ساخت ')
    last_join = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    
    object = MyAccountManeger()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, add_label):
        return True