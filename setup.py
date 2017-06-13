from setuptools import setup
import os

setup(name='adsputils',
      version='0.0.1',
      packages=['adsputils'],
      install_requires=[
          'ConcurrentLogHandler==0.9.1',
          'python-dateutil==2.6.0',
          'DateTime==4.1.1'
      ]
  )