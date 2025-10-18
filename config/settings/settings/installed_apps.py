DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.courses",
]

THIRD_PARTY = [
    "rest_framework",
    "debug_toolbar",
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY



