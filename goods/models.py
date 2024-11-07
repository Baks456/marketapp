from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse_lazy


# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Категория')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    sort_level = models.PositiveIntegerField(default=0, verbose_name='Уровень для сортировки')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['-sort_level', 'name']

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse_lazy('goods:catalog', kwargs={'cat_slug': self.slug})


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, blank=False, verbose_name='Название продукта')
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images/%Y/%m/%d/', default=None, blank=True, null=True,
                              verbose_name='Изображение товара')
    price = models.DecimalField(default=1000000, max_digits=12, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.0, max_digits=5, decimal_places=2, verbose_name='Скидка в %',
                                   validators=[MinValueValidator(0), MaxValueValidator(100)])
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-price', 'name', ]

    def display_id(self):
        return f'{self.id:06}'

    def real_price(self):
        if self.discount:
            return round((self.price - self.price * self.discount / 100), 2)
        return self.price

    def get_absolute_url(self):
        return reverse_lazy('goods:product', kwargs={'product_slug': self.slug})
