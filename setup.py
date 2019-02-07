try:
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description': 'Module for special ping in Linux or Windows.',
    'author': 'Sergey Trishkin',
    'url': 'https://github.com/grdvsng/EasyPing',
    'download_url': 'https://github.com/grdvsng/EasyPing',
    'author_email': 'grdvsng@gmail.com',
    'version': '0.8',
    'install_requires': ['easyping'],
    'packages': ['easyping'],
    'name': 'easyping',
}

setup(**config)