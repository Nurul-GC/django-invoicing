#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='django-invoicing',
    version='3.0.0',
    description='Django app for invoicing.',
    long_description=open('README.rst').read(),
    author='Pragmatic Mates',
    author_email='info@pragmaticmates.com',
    maintainer='Pragmatic Mates',
    maintainer_email='info@pragmaticmates.com',
    url='https://github.com/PragmaticMates/django-invoicing',
    packages=find_packages(),
    include_package_data=True,
    install_requires=(
        'django>=3.1', 'django-countries', 'django-iban', 'django-model-utils', 'django-money', 'vatnumber'
    ),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha'
    ],
    license='GPL License',
    keywords="django invoice invoicing billing supplier issuer purchaser buyer commerce products taxes vat pdf",
)
