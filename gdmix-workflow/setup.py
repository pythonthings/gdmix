from pathlib import Path
from setuptools import find_namespace_packages, setup
from sys import platform as _platform
from sys import version_info as _py_version

import sys


VERSION="0.2.1"
current_dir = Path(__file__).resolve().parent
with open(current_dir.joinpath('README.md'), encoding='utf-8') as f:
    long_description = f.read()

if _py_version < (3, 3):
    print('\nrequires at least Python 3.3!')
    sys.exit(1)

if _platform not in ["linux", "linux2", "darwin"]:
    print("ERROR: platform {} isn't supported".format(_platform))
    sys.exit(1)

setup(
    name="gdmix-workflow",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=["Programming Language :: Python :: 3.7",
                 "Intended Audience :: Science/Research",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved"],
    license='BSD-2-CLAUSE',
    version=f'{VERSION}',
    package_dir={'': 'src'},
    packages=find_namespace_packages(where='src'),
    package_data={'': ['*.yaml']},
    include_package_data=True,
    install_requires=[
        "setuptools>=41.0.0",
        f"gdmix-trainer=={VERSION}",
        "google-auth==1.21.1",
        "kfp==0.2.5"
    ],
    tests_require=['pytest']
)
