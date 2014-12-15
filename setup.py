#!/usr/bin/env python

from setuptools import setup, find_packages

# one line description
description = "tools for Mad & Kea"

version = 0.01

setup(name='toMaKe',
      version=version,
      description=description,
      author='Mark Fiers',
      author_email='mark.fiers.42@gmail.com',
      include_package_data=True,
      packages=find_packages(),
      install_requires=[
          'Leip',
          'lockfile',
          'fantail',
          'grako>3',
          'humanize',
          'jinja2',
          'psutil',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
      ]
      )
