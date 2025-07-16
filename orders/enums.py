from django.db import models


class Material(models.TextChoices):
    PLA = 'pla', 'PLA'
    ABS = 'abs', 'ABS'
    PETG = 'petg', 'PETG'
    RESIN = 'resin', 'Resin'


class Quality(models.TextChoices):
    DRAFT = '0.3', 'Черновое (0.3мм)'
    STANDARD = '0.2', 'Стандартное (0.2мм)'
    HIGH = '0.15', 'Высокое (0.15мм)'
    ULTRA = '0.1', 'Ультра (0.1мм)'


class OrderStatus(models.TextChoices):
    NEW = 'new', 'Новый'
    IN_REVIEW = 'in_review', 'В обработке'
    PRINTING = 'printing', 'Печать'
    SHIPPED_TO_DELIVERY = 'shipped_to_delivery', 'Отправлено в доставку'
    IN_DELIVERY = 'in_delivery', 'Доставляется'
    DELIVERED = 'delivered', 'Доставлен'
    DONE = 'done', 'Выполнен'
    REFUND = 'refund', 'Возврат'
