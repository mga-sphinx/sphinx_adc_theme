# -*- coding: utf-8 -*-
"""`sphinx_adc_theme` lives on `Github`_.

.. _github: https://github.com/mga-sphinx/sphinx_adc_theme

"""
from setuptools import setup


setup(
    name='sphinx_adc_theme',
    url='https://github.com/mga-sphinx/sphinx_adc_theme',
    license='BSD',
    author='Christophe CHAUVET',
    author_email='christophe.chauvet@gmail.com',
    description='Apple Developer Connection theme for Sphinx, 2015 version.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    keywords='sphinx theme',
    packages=['sphinx_adc_theme'],
    package_data={
        'sphinx_adc_theme': [
            'theme.conf',
            '*.html',
            'static/css/*.css',
            'static/js/*.js',
            'static/img/*.*'
        ]
    },
    include_package_data=True,
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    classifiers=[
        'Development Status :: 3 - Beta',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_adc_theme = sphinx_adc_theme',
        ]
    },
)
