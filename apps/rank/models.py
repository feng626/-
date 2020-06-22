from common import models
from user.models import User


class Fraction(models.BaseModel):
    value = models.PositiveIntegerField(help_text="分数值")
    user = models.OneToOneField(User, on_delete=models.PROTECT,
                                related_name='fractions', help_text="用户")

    class Meta:
        verbose_name = verbose_name_plural = '分数'
        db_table = 'fraction'
        ordering = ["-value"]
