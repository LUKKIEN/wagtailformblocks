#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

install_requires = [
    'wagtail>=1.0',
    'django-model-utils>=2.5.2',
]

test_require = [
    # For coverage and PEP8 linting
    'coverage>=3.7.0',
    'flake8>=2.2.0',
    'isort>=4.2.0',
    'tox>=2.3.1',
    'cryptography==1.4',
    'PyYAML==3.11',
    'bumpversion==0.5.3',
    'wheel==0.29.0',
    'watchdog==0.8.3',
]

docs_require = [
    'sphinx',
    'sphinx_rtd_theme',
]

setup(
    name='wagtailformblocks',
    version='0.1.2',
    description="A Wagtail module that provides content blocks to display and process user defined forms", # NOQA
    long_description=readme + '\n\n' + changelog,
    author="Tim Leguijt",
    author_email='info@leguijtict.nl',
    url='https://github.com/LUKKIEN/wagtailformblocks',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=install_requires,
    license='BSD',
    zip_safe=False,
    keywords='wagtailformblocks',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    extras_require={
        'testing': test_require,
        'docs': docs_require,
    },
)
