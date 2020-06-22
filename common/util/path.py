import os


def dirname(base, repeat=1):
    dir_name = base
    while repeat > 0:
        dir_name = os.path.dirname(dir_name)
        repeat -= 1

    return dir_name
