import os

from django.urls import path, include


def inc_all_urls(file):
    apps_dir = os.path.dirname(file)

    apps = os.listdir(apps_dir)

    urls = [path('', include(f'{app}.urls'))
            for app in apps if not app.startswith(('_', '.'))]
    return urls
