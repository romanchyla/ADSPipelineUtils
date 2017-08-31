from setuptools import setup
import os


# hack: we can't use github in the install_requires section; so until we have an official 
# release of ADSPipelineMsg package available, this has to suffice... 
os.system('pip install --upgrade git+https://github.com/romanchyla/ADSPipelineMsg.git@foo')

setup(name='adsputils',
      version='0.0.1',
      packages=['adsputils'],
      install_requires=[
          'ConcurrentLogHandler==0.9.1',
          'python-dateutil==2.6.0',
          'DateTime==4.1.1',
          'celery==4.0.2',
          #'ADSPipelineMsg==1.0.0',
          'SQLAlchemy==1.1.6'
          
      ],
      #entry_points={
      #      'kombu.serializers': [
      #          'adsmsg = adsputils.serializer:register_args'
      #      ]
      #  }
  )
