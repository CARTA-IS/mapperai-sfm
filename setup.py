#!/usr/bin/env python

from __future__ import print_function

import errno
import os
import setuptools
import subprocess
import sys
from wheel.bdist_wheel import bdist_wheel


class platform_bdist_wheel(bdist_wheel):
    """Patched bdist_well to make sure wheels include platform tag."""
    def finalize_options(self):
        bdist_wheel.finalize_options(self)
        self.root_is_pure = False


def mkdir_p(path):
    """Make a directory including parent directories."""
    try:
        os.makedirs(path)
    except os.error as exc:
        if exc.errno != errno.EEXIST or not os.path.isdir(path):
            raise

print( "Configuring...")
mkdir_p('cmake_build')
subprocess.Popen(['cmake','../opensfm/src'], cwd='cmake_build').wait()

print( "Compiling extension...")
subprocess.Popen(['make','-j4'], cwd='cmake_build').wait()

print ("Building package")
setup(
    name='OpenSfM',
    version='0.1',
    description='A Structure from Motion library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mapillary/OpenSfM',
    project_urls={
        "Documentation": "https://docs.opensfm.org/",
    },
    author='Mapillary',
    license='BSD',
    packages=setuptools.find_packages(),
    scripts=[
        'bin/opensfm_run_all',
        'bin/opensfm',
    ],
    package_data={
        'opensfm': [
            'csfm.*',
            'data/sensor_data.json',
            'data/bow/bow_hahog_root_uchar.npz',
        ]
    },
    # install_requires=[
    #     'cloudpickle>=0.4.0',
    #     'ExifRead>=2.1.2',
    #     'gpxpy>=1.1.2',
    #     'loky>=1.2.1',
    #     'networkx>=1.11',
    #     'numpy>=1.13',
    #     'pyproj>=1.9.5.1',
    #     'pytest>=3.0.7',
    #     'python-dateutil>=2.6.0',
    #     'PyYAML>=3.12',
    #     'repoze.lru>=0.7',
    #     'scipy',
    #     'six',
    #     'xmltodict>=0.10.2',
    #     'Pillow>=6.0.0',
    # ],
    cmdclass={'bdist_wheel': platform_bdist_wheel},
)
