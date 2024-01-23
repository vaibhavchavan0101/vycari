# pylint: skip-file
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8c8c11e3-5859-4feb-8d17-301fe1df2a80'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

ALLOWED_HOSTS = ['*']
