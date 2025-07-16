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
    NEW = "Новый"
    IN_REVIEW = "В обработке"
    PRINTING = "Печать"
    SHIPPED_TO_DELIVERY = "Отправлено в доставку"
    IN_DELIVERY = "Доставляется"
    DELIVERED = "Доставлен"
    DONE = "Выполнен"
    RETURNED = "Возврат"
