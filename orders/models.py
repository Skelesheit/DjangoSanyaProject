from django.db import models
from orders.enums import Material, Quality, OrderStatus
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=20)
    telegram = models.CharField(max_length=40)

    class Meta:
        verbose_name = _("Контакт")
        verbose_name_plural = _("Контакты")


class PrintFile(models.Model):
    file = models.FileField()
    filename = models.CharField(max_length=200)
    size = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
    note = models.TextField(max_length=200)  # наше примечание

    class Meta:
        verbose_name = _("Файл")
        verbose_name_plural = _("Файлы")


class Order(models.Model):
    material = models.CharField(max_length=20, choices=Material)
    quality = models.CharField(max_length=20, choices=Quality)
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True, null=True)

    contact = models.ManyToOneRel(Contact, on_delete=models.CASCADE, related_name="orders")
    files = models.ManyToManyRel(PrintFile,  related_name="orders")

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self):
        return f"Order #{self.id} ({self.material}, {self.quality})"


class OrderHistory(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    status = models.IntegerField(choices=OrderStatus, default=OrderStatus.NEW)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="history")

    class Meta:
        verbose_name = _("Сторипоинт")
        verbose_name_plural = _("Сторипоинты")

    def __str__(self):
        return f"{self.get_status_display()} @ {self.timestamp}"
