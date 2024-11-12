from django.contrib.auth import get_user_model
from django.db import models

from goods.models import Products


# Create your models here.

class OrderItemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class DeliveryStatus(models.TextChoices):
    FORMED = '10', 'заказ сформирован'
    IN_DELIVERY = '20', 'в доставке'
    WAITING = '50', 'ожидает получения'
    COMPLETE = '100', 'доставлен'


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, blank=True, null=True,
                             verbose_name="Пользователь",
                             default=None)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания заказа")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    required_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    payment_on_delivery = models.BooleanField(default=False, verbose_name="Оплата при получении")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    status = models.CharField(max_length=20, choices=DeliveryStatus, default='10', verbose_name='Статус заказа')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ("id",)

    def __str__(self):
        return f"Заказ № {self.pk} | Покупатель {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, null=True, verbose_name="Продукт",
                                default=None)
    name = models.CharField(max_length=150, verbose_name="Название")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата продажи")

    class Meta:
        verbose_name = "Проданный товар"
        verbose_name_plural = "Проданные товары"
        ordering = ("id",)

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return round(self.product.real_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} | Заказ № {self.order.pk}"
