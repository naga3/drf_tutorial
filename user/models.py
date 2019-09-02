from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, help_text='名前')
    birth_date = models.DateField(null=True, blank=True, help_text='誕生日')
    created_at = models.DateTimeField(auto_now_add=True, help_text='作成日時')
    updated_at = models.DateTimeField(auto_now=True, help_text='更新日時')
