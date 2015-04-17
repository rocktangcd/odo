#!/usr/bin/env python

import os
from fnmatch import fnmatch
from setuptools import setup, find_packages

import versioneer
versioneer.VCS = 'git'
versioneer.versionfile_source = os.path.join('odo', '_version.py')
versioneer.versionfile_build = versioneer.versionfile_source
versioneer.tag_prefix = ''  # tags are like 1.2.0
versioneer.parentdir_prefix = 'odo-'  # dirname like 'myproject-1.2.0'


def find_data_files(where, exts):
    exts = tuple(exts)
    for root, dirs, files in os.walk(where):
        for f in files:
            if any(fnmatch(f, pat) for pat in exts):
                yield os.path.join(root, f)


exts = ('*.h5', '*.csv', '*.xls', '*.xlsx', '*.db', '*.json', '*.gz', '*.hdf5',
        '*.sas7bdat')
package_data = [x.replace('odo' + os.sep, '') for x in
                find_data_files('odo', exts)]


def read(filename):
    with open(filename, 'r') as f:
        return f.read()


setup(name='odo',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Data migration utilities',
      url='http://github.com/ContinuumIO/odo',
      author='Blaze development deam',
      author_email='blaze-dev@continuum.io',
      license='BSD',
      keywords='odo data conversion hdf5 sql blaze',
      packages=find_packages(),
      install_requires=read('requirements.txt').strip().split('\n'),
      long_description=(read('README.rst')
                        if os.path.exists('README.rst')
                        else ''),
      package_data={'odo': package_data},
      zip_safe=False,
      scripts=[os.path.join('bin', 'odo')])
