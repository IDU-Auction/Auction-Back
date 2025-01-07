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
