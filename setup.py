# -*- coding: utf-8 -*-
"""`sphinx_adc_theme` lives on `Github`_.

.. _github: https://github.com/mga-sphinx/sphinx_adc_theme

"""
from setuptools import setup
from sphinx_adc_theme import __version__


setup(
    name='sphinx_adc_theme',
    version=__version__,
    url='https://github.com/mga-sphinx/sphinx_adc_theme',
    license='BSD',
    author='Christophe CHAUVET',
    author_email='christophe.chauvet@gmail.com',
    description='Apple Developer Connection theme for Sphinx, 2015 version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    keywords = 'sphinx theme',
    packages=['sphinx_adc_theme'],
    package_data={'sphinx_adc_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/img/*.*'
    ]},
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
