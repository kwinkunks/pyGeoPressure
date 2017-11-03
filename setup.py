#!/usr/bin/env python
"""
Created on Nov 1st 2017
"""

from distutils.core import setup
from setuptools import find_packages


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Physics',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS',
    'Natural Language :: English',
]

with open("README.md") as f:
    LONG_DESCRIPTION = ''.join(f.readlines())

setup(
    name="pyGeoPressure",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.7',
        'scipy>=0.13',
        'matplotlib',
        'segpy'
    ],
    author="Yu Hao",
    author_email="yuhao@live.cn",
    description="pyGeoPressure: Tools for geopressure prediction",
    long_description=LONG_DESCRIPTION,
    license="MIT",
    keywords="pore pressure prediction",
    url="https://github.com/whimian/pyGeoPressure",
    download_url="https://github.com/whimian/pyGeoPressure",
    classifiers=CLASSIFIERS,
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    use_2to3=False
)