try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'CLI based Wordpress publisher',
    'author': 'Balasankar C',
    'url': 'http://gitlab.com/balasankarc/publish2wp',
    'download_url': 'http://gitlab.com/balasankarc/publish2wp',
    'author_email': 'balasankarc@autistici.org',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['publish2wp'],
    'scripts': ['bin/p2wp'],
    'name': 'publish2wp'
}

setup(**config)
