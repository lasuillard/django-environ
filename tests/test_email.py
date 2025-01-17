# This file is part of the django-environ.
#
# Copyright (c) 2021-2024, Serghei Iakovlev <oss@serghei.pl>
# Copyright (c) 2013-2021, Daniele Faraglia <daniele.faraglia@gmail.com>
#
# For the full copyright and license information, please view
# the LICENSE.txt file that was distributed with this source code.

from environ import Env


def test_smtp_parsing():
    url = 'smtps://user@domain.com:password@smtp.example.com:587'
    url = Env.email_url_config(url)

    assert len(url) == 7

    assert url['EMAIL_BACKEND'] == 'django.core.mail.backends.smtp.EmailBackend'
    assert url['EMAIL_HOST'] == 'smtp.example.com'
    assert url['EMAIL_HOST_PASSWORD'] == 'password'
    assert url['EMAIL_HOST_USER'] == 'user@domain.com'
    assert url['EMAIL_PORT'] == 587
    assert url['EMAIL_USE_TLS'] is True
    assert url['EMAIL_FILE_PATH'] == ''


def test_custom_email_backend():
    """Override EMAIL_BACKEND determined from schema."""
    url = 'smtps://user@domain.com:password@smtp.example.com:587'

    backend = 'mypackage.backends.whatever'
    url = Env.email_url_config(url, backend=backend)

    assert url['EMAIL_BACKEND'] == backend
