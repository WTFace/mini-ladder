from django.db import models
from django.utils import timezone


class Result(models.Model):
    class Meta:
        verbose_name = "결과"
        verbose_name_plural = "결과"

    def __str__(self):
        return str(self.id)

    TYPE_START = (
        ('L', '좌'),
        ('R', '우'),
    )
    BRIDGE_COUNT = (
        (3, 3),
        (4, 4),
    )

    start = models.CharField('출발', max_length=4,choices=TYPE_START, default='L')
    bridges = models.IntegerField('다리수', choices=BRIDGE_COUNT, default=3)

