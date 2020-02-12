#!/usr/bin/env python

from setuptools import setup, Extension

setup(name='fcntl',
      version='1.0',
      description='fcntl for windows',
      author='Zou Guangxian',
      author_email='zouguangxian@163.com',
      url='',
      ext_modules=[Extension('fcntl', 
            ['src/fcntlmodule.c', 'src/flock.c', 'src/msvc-inval.c', 'src/msvc-nothrow.c'], 
            include_dirs=['src'],
            libraries=['Ws2_32'])],
     )