# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='simplexmldsig',
      packages=['simplexmldsig'],
      version='0.1',
      author=u'Greendizer',
      author_email='developers@xmli.com',
      install_requires=['pycrypto >= 2.6',
                        'lxml >= 2.3'],
      url='http://github.com/alx242/simplexmldsig',
      license=open('LICENCE').read(),
      description='Sign xml documents with a xmldsig',
      zip_safe=True,
      )
