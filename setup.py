import os
from setuptools import setup


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="fernetstring",
    version="0.2.0",
    author="James Riach",
    author_email="james@jriach.co.uk",
    description=("A simple library used to encrypt strings"),
    install_requires=[
        "cryptography"
    ],
    license="",
    url="",
    packages=['fernetstring', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
    test_suite='tests',
)
