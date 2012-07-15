# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='pyxmli',
    packages=find_packages(),
    version='0.0.1',
    author=u'Greendizer',
    author_email='developers@greendizer.com',
    packages=['pyxmli'],
    install_requires=['pycrypto >= 2.5', 'lxml >= 2.3'],
    url='http://github.com/Greendizer/PyXMLi',
    license=open('licence.txt').read(),
    description='Create and sign XMLi invoices in Python.',
    long_description=open('README.markdown').read(),
    zip_safe=True,
)