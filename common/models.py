from django.db.models import * # NOQA


class BaseModel(Model):
    create_by = CharField(max_length=255, default='jic')
    create_time = DateTimeField(auto_now_add=True)
    update_by = CharField(max_length=255, default='jic')
    update_time = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)
