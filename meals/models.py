from django.db import models
from django.utils.text import slugify


# Create your models here.

class Meals(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    price = models.TextField()

    image = models.ImageField(upload_to='meals/',null=True,blank=True)
    slug = models.SlugField(blank=True,null=True)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'meals'
        verbose_name_plural= 'meals'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Meals,self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
