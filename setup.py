import pathlib

from setuptools import find_packages, setup


here = pathlib.Path(__name__).absolute().parent


setup(
    # Basics
    name='crystalball',
    description='A Python library to guess data from inconsistent structures',
    long_description=(here / 'README.md').read_text(),
    version='0.0.0',

    # Package finding
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Testing
    setup_requires=['pytest-runner'],
    tests_require=['coverage', 'pytest'],

    # Project info
    url='https://github.com/7ws/python-crystalball',
    author='Evandro Myller',
    author_email='emyller@7ws.co',
    license='MIT',

    # Classifiers
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',  # TODO: Make it production-ready
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing',
        'Topic :: Utilities',
    ],
)
