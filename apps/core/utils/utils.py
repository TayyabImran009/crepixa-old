import json
import uuid
from typing import Optional

import requests

from django.conf import settings
from django.core.cache import cache
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.utils.text import slugify

__all__ = (
    'get_file_path',
    'get_image_from_url',
    'build_client_absolute_url',
    'to_usd',
    'from_usd',
    'rates_data',
)


def get_file_path(instance, filename: str) -> str:
    model = type(instance)
    upload_dir = '{}/{}'.format(
        slugify(model._meta.app_label),
        slugify(model.__name__)
    )

    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4(), ext)
    return 'images/{}/{}'.format(upload_dir, filename)


def get_image_from_url(url: str) -> Optional[File]:
    response = requests.get(url)

    if response.status_code == 200:

        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(response.content)
        img_temp.flush()

        return File(img_temp)

    return None


def build_client_absolute_url(path: str) -> str:
    domain = settings.CLIENT_DOMAIN
    url_scheme = settings.URL_SCHEME

    return '{url_scheme}://{domain}{path}'.format(
        url_scheme=url_scheme,
        domain=domain,
        path=path,
    )


def get_rates():
    url = f'http://data.fixer.io/api/latest?symbols=USD,RUB,EUR,AMD&access_key={settings.FIXER_KEY}'
    response = requests.get(url)
    if response.status_code != 200 or not response.json().get('success'):
        return {
            'success': True,
            'base': "EUR",
            'date': "2019-09-29",
            'rates': {
                'USD': 1.094103,
                'RUB': 70.745932,
                'EUR': 1,
                'AMD': 520.432593,
            },
        }
    return response.json()


def to_usd(currency: str) -> float:
    rates = cache.get('rates', None)
    if rates:
        rates = json.loads(rates)
    else:
        rates = get_rates()
        cache.set('rates', json.dumps(rates), 24 * 60 * 60)  # 24 hours

    return float(rates['rates']['USD']) / float(rates['rates'].get(currency, 1))


def from_usd(currency: str) -> float:
    rates = cache.get('rates', None)

    if rates:
        rates = json.loads(rates)
    else:
        rates = get_rates()
        cache.set('rates', json.dumps(rates), 24 * 60 * 60)  # 24 hours

    return float(rates['rates'].get(currency, 1) / rates['rates']['USD'])


def rates_data() -> dict:
    rates = cache.get('rates', None)
    if rates:
        rates = json.loads(rates)
    else:
        rates = get_rates()
        cache.set('rates', json.dumps(rates), 24 * 60 * 60)  # 24 hours

    return rates['rates']
