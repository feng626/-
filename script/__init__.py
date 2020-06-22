from django.db.utils import IntegrityError


def run_standalone():
    import os
    import sys
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview.settings')
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir))
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    os.pardir, 'apps'))
    django.setup()


run_standalone()


class InitBase():
    objs = tuple()
    model_cls = None

    def run(self):
        for obj in self.objs:
            try:
                self.create(obj)
            except IntegrityError:
                # 处理重复数据
                pass

    def create(self, obj):
        self.model_cls.objects.create(**obj)
