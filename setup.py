# -*- coding: utf-8 -*-

from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Word Game Solver',
    'author': 'Alexandros Bourantas',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'buritos@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['game'],
    'scripts': [],
    'name': 'WordGame'
}

setup(**config)

