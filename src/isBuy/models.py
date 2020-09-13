from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Requests(models.Model):
    # usersテーブルとのリレーション
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        verbose_name='題名',
        max_length=100
    )

    category = models.IntegerField(
        verbose_name='申請区分',
    )

    price = models.IntegerField(
        verbose_name='金額',
    )

    body = models.TextField(
        verbose_name='本文',
        max_length=150
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.price}円の申請'

# request_commentsテーブル

# request_filesテーブル
