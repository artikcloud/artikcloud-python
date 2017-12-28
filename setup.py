# coding: utf-8

"""
    ARTIK Cloud API

    This SDK helps you connect your Python scripts to ARTIK Cloud. 
    The SDK helps authenticating with ARTIK Cloud, and exposes a number of methods to easily execute REST API 
    calls to ARTIK Cloud.

    
    https://github.com/artikcloud/artikcloud-python
    
"""


import sys
from setuptools import setup, find_packages

NAME = "artikcloud"
VERSION = "2.2.3"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="ARTIK Cloud API",
    author_email="",
    url="",
    keywords=["ARTIK Cloud API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    ARTIK Cloud Python SDK
    """
)
