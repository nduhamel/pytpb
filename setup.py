#!/usr/bin/env python

import os

from distutils.core import setup
from pytpb import __version__, __maintainer__, __license__

setup(name='pytpb',
      description='python client for thepiratebay.org website',
      long_description = file(
          os.path.join(os.path.dirname(__file__),'README')).read(),
      license=__license__,
      version=__version__,
      maintainer=__maintainer__,
      url='https://github.com/nduhamel/pytpb',
      packages=['pytpb'],
      classifiers = [
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Operating System :: OS Independent'
      ]
     )

