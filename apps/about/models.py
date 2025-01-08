from django.db import models


class About(models.Model):

    name = models.CharField("Название", max_length=255)

    class Meta:
        ordering = ['id',]
        verbose_name = "О нас"
        verbose_name_plural = "О нас"
    
    def __str__(self):
        return self.name


class Text(models.Model):

    text_types = (
        ('privacy', 'privacy'),
        ('terms', 'terms'),
        ('cookies', 'cookies'),
    )

    text_type = models.CharField("Тип текста", max_length=255, choices=text_types)
    text = models.TextField("Текст")

    class Meta:
        ordering = ['id',]
        verbose_name = "Текст"
        verbose_name_plural = "Текст"
    
    def __str__(self):
        return self.text_type


class Subject(models.Model):

    status_types = (
        ('active', 'active'),
        ('deactive', 'deactive'),
    )

    order = models.IntegerField("Очередь", default=0)
    name = models.CharField("Название", max_length=255)
    status = models.CharField("Статус", max_length=255, choices=status_types, default='active')

    class Meta:
        ordering = ['order',]
        verbose_name = "Тема"
        verbose_name_plural = "Темы"

    def __str__(self) -> str:
        return self.name


class Message(models.Model):

    name = models.CharField("Имя", max_length=255)
    email = models.EmailField("Почта", max_length=255)
    phone_number = models.CharField("Телефон", max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.RESTRICT, verbose_name="Тема")
    message = models.TextField("Сообщение")
    date = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        ordering = ['id',]
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self) -> str:
        return self.name
