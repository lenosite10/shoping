from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصول'
    
    category_name = models.CharField(max_length=100,unique=True,verbose_name='نام دسته بندی ')
    slug = models.SlugField(max_length=100,unique=True,verbose_name='تقسیم بندی کردن  نام دسته بندی')
    description = models.TextField(max_length=255, unique=True,verbose_name='توضیحات ')
    cat_image = models.ImageField(upload_to='photo/categories', unique=True,verbose_name='عکس دسته بندی ')
    
    def get_url(self):
        return reverse('product_by_category', args=[self.slug])
    
    def __str__(self):
        return self.category_name