#!/usr/bin/env python

from setuptools import setup

setup(
        name='GNOMEUtils',
        version='0.2.0',
        description='Various utilities for working with GNOME.',
        author='Jeremy Cantrell',
        author_email='jmcantrell@gmail.com',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: X11 Applications :: Gnome',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Natural Language :: English',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Topic :: Desktop Environment :: Gnome',
            ],
        packages=[
            'gnomeutils',
            ],
        )
