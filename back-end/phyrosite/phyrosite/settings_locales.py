# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wegao+1)v=u=6k7)l!afl^quqke7gn&!$q4wl$g-a203)@+(bw'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}