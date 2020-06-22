from script import run_standalone # NOQA
from script import init_user

INIT_ALL = 2


def init():
    init_user.run()


if __name__ == '__main__':
    init()
