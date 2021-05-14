from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Coupon(models.Model):
    code = models.CharField(max_length=200, unique=True)
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    acteve = models.BooleanField()

    class Meta:
        verbose_name = 'Coupon'
        verbose_name_plural = 'Coupons'

    def __str__(self):
        return self.code




