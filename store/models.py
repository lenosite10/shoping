from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    class Meta:
        verbose_name = 'محصول گذاری'
        verbose_name_plural = 'محصول گذاری'
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name='دسته بندی ها')
    product_name = models.CharField(max_length=255,unique=True,verbose_name='نام محصول')
    slug = models.SlugField(max_length=255,unique=True,verbose_name='نام محصل اسلگ')
    description = models.TextField(max_length=5000,blank=True,verbose_name='توضیحات محصول')
    price = models.IntegerField(verbose_name='قیمت')
    price_old = models.IntegerField(verbose_name='قیمت قدیمی',null=True)
    images = models.ImageField(upload_to='photo/products',verbose_name='عکس محصول')
    stock = models.IntegerField( verbose_name='تعداد موجود')
    is_available = models.BooleanField(default=True,verbose_name='آیا موجود است')
    
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    modifired_date = models.DateTimeField(auto_now=True, verbose_name='زمان ویرایش')
    
    def get_url(self):
        return reverse('detail_product',args=[self.category.slug, self.slug])


    def __str__(self):
        return self.product_name

