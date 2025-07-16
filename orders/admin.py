from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin

from .models import Order, Contact, PrintFile, OrderHistory


# Вложенные модели
class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0
    max_num = 1  # Один контакт на заказ
    verbose_name = _("Контакт")
    verbose_name_plural = _("Контакт")


class PrintFileInline(admin.TabularInline):
    model = PrintFile
    extra = 1  # сколько пустых строк по умолчанию
    fields = ("file", "filename", "size", "count", "note")
    verbose_name = "Файл"
    verbose_name_plural = "Файлы"



class OrderHistoryInline(admin.TabularInline):
    model = OrderHistory
    extra = 0
    readonly_fields = ("timestamp",)
    can_delete = False
    verbose_name = _("История статуса")
    verbose_name_plural = _("История статуса")


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    inlines = [ContactInline, PrintFileInline, OrderHistoryInline]

    list_display = ("id", "material", "quality", "count", "created_at", "get_latest_status_display")
    list_filter = ("material", "quality", "history__status")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    search_fields = ("id", "contact__name", "contact__email")
    icon = 'package'

    fieldsets = (
        (_("Информация о заказе"), {
            "fields": ("material", "quality", "count", "note"),
        }),
        (_("Служебное"), {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )

    def get_latest_status_display(self, obj):
        latest = obj.history.order_by("-timestamp").first()
        return latest.get_status_display() if latest else "-"

    get_latest_status_display.short_description = _("Статус")


@admin.register(PrintFile)
class PrintFileAdmin(ModelAdmin):
    inlines = []
    list_display = ("filename", "order", "size", "count", "created_at")
    list_filter = ("created_at", "order__material", "order__quality")
    search_fields = ("filename", "order__id")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    icon = 'file'

    fieldsets = (
        (_("Файл"), {
            "fields": ("file", "filename", "size", "count", "note"),
        }),
        (_("Связь"), {
            "fields": ("order",),
        }),
        (_("Служебное"), {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ("name", "email", "phone", "telegram", "order")
    list_filter = ("order",)
    search_fields = ("name", "email", "telegram", "order__id")
    icon = 'user'

    fieldsets = (
        (_("Контактная информация"), {
            "fields": ("name", "email", "phone", "telegram"),
        }),
        (_("Заказ"), {
            "fields": ("order",),
        }),
    )


@admin.register(OrderHistory)
class OrderHistoryAdmin(ModelAdmin):
    list_display = ("order", "status_display", "timestamp")
    list_filter = ("status", "timestamp")
    search_fields = ("order__id",)
    ordering = ("-timestamp",)
    icon = 'history'

    readonly_fields = ("timestamp",)

    fieldsets = (
        (_("История статуса"), {
            "fields": ("order", "status", "timestamp"),
        }),
    )

    def status_display(self, obj):
        return obj.get_status_display()

    status_display.short_description = _("Статус")
