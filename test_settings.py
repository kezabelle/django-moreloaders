# -*- coding: utf-8 -*-
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": None,
    }
}

INSTALLED_APPS = (
    "moreloaders",
)

SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.MD5PasswordHasher",
)

MOSTLYCACHED_EXCLUDES = (
    r'^.+\.json$',
    r'^.+\.shtml$',
    r'^other.+$',
    r'^x[a-z]{1,2}.html$',
    r'^y[a|b].html$',
)
