#!/usr/bin/env python

from setuptools import setup, find_packages
from glob import glob

setup(
        name='GNOMEUtils',
        version='0.1.5',
        description='Various small utilities for working with GNOME.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: X11 Applications :: Gnome',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Desktop Environment :: Gnome',
            ],
        packages=[
            'gnomeutils',
            ],
        )
