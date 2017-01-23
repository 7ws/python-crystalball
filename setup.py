import pathlib

from setuptools import find_packages, setup


here = pathlib.Path(__name__).absolute().parent


setup(
    name='crystalball',
    description='A Python library to guess data from inconsistent structures',
    long_description=(here / 'README.md').read_text(),
    version='0.0.0',

    # Package finding
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Testing
    setup_requires=['pytest-runner'],
    tests_require=['coverage', 'pytest'],
)
