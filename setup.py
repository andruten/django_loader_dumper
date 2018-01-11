from distutils.core import setup
from setuptools import find_packages


setup(
    name='django_loader_dumper',
    packages=find_packages(),
    version='1.0',
    description='Commands for loading and dumping fixtures based on app names.',
    author='Andruten',
    author_email='andusaben@gmail.com',
    url='https://github.com/andruten/django_loader_dumper',
    download_url='https://github.com/andruten/django_loader_dumper/archive/1.0.tar.gz',
    keywords=['django', 'fixtures', 'dumpdata', 'loaddata', 'commands', 'json'],
    classifiers=[],
)
