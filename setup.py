#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

install_requires = [
    'django-model-utils>=4.2,<4.4',
    'django-recaptcha>=3.0,<3.1',
    'wagtail>=4.0,<4.3',
    'django>=3.2,<5'
]

test_require = [
    'psycopg2-binary',
    # Required for test and coverage
    'pytest',
    'pytest-cov',
    'pytest-django',
    'pytest-pythonpath',
    'coverage',
    'factory-boy',
    'tox',
    # Linting
    'flake8',
    'isort',
]

docs_require = [
    'sphinx',
    'sphinx_rtd_theme',
]

setup(
    name='wagtailformblocks',
    version='0.8.0',
    description="A Wagtail module that provides content blocks to display and process user defined forms",
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
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 4',
    ],
    extras_require={
        'testing': test_require,
        'docs': docs_require,
    },
)
