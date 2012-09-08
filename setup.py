# -*- coding: utf-8 -*-
try:
    from distutils.core import setup
except ImportError:
    from setuptools import setup

setup(
    name                = 'pyxmli',
    packages            = ['pyxmli'],
    version             = open('VERSION').read(),
    author              = u'Greendizer',
    author_email        = 'developers@xmli.com',
    packages            = ['pyxmli'],
    package_data        = {'pyxmli' : ['../VERSION']},
    install_requires    = ['pycrypto >= 2.6',
                           'lxml >= 2.3'],
    url                 = 'http://github.com/Greendizer/PyXMLi',
    license             = open('LICENCE').read(),
    description         = 'Create and sign XMLi invoices in Python.',
    long_description    = open('README.markdown').read(),
    zip_safe            = True,
    test_suite          = 'tests'
)