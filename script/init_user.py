from django.db.transaction import atomic
from script import InitBase
from user.models import User
from rank.models import Fraction


class InitUser(InitBase):
    model_cls = User
    objs = (
        {'id': 2, 'username': 'test002', 'no': '2', 'password': '123',
         'email': '0002@.com'},
        {'id': 3, 'username': 'test003', 'no': '3', 'password': '123',
         'email': '0003@.com'},
        {'id': 4, 'username': 'test004', 'no': '5', 'password': '123',
         'email': '0004@.com'},
        {'id': 5, 'username': 'test005', 'no': '6', 'password': '123',
         'email': '0005@.com'},
        {'id': 6, 'username': 'test006', 'no': '7', 'password': '123',
         'email': '0006@.com'},
        {'id': 7, 'username': 'test007', 'no': '8', 'password': '123',
         'email': '0007@.com'},
        {'id': 8, 'username': 'test008', 'no': '9', 'password': '123',
         'email': '0008@.com'}
    )

    @atomic
    def create(self, obj):
        user = self.model_cls.objects.create(**obj)
        user.set_password(obj['password'])
        user.save()
        Fraction.objects.create(value=0, user=user)


def run():
    InitUser().run()


if __name__ == '__main__':
    run()
