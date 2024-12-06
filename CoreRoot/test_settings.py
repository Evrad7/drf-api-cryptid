from .settings import *



DATABASES = {
    'default': {
        'ENGINE':"django.db.backends.postgresql",
        'NAME':"django_api",
        "USER":"django_api_user_test",
        "PASSWORD":"django_api_user_test",
        "HOST":"localhost",
        "POST":"5432",
    }
}
