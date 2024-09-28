from django.db import models
from django.contrib.auth.models import User


class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='updated_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'item'
        verbose_name = "item"
        verbose_name_plural = "item"
        ordering = ["id"]