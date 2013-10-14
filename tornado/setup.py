import os
from setuptools import setup, find_packages
install_requires = []

install_requires.append('tornado')
install_requires.append('praw')
# pip install requests giphypop
install_requires.append('requests')
install_requires.append('giphypop')

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')
description = 'Attempt to learn about Search Engines & their user base.'

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description

setup(
    name = 'Dubsit',
    version = '0.0.1',
    install_requires = install_requires,
    description = description,
    long_description = long_description,
    author = 'Abhi Agarwal',
    author_email = 'hi@abhi.co',
    url = 'http://www.dubsit.com/',
    packages = ['dubsit'],
)