import os
import sys
from setuptools import find_packages, setup

setup(
    name='slackline',
    version="1.0.0",
    url='FIXME',
    author='FIXME',
    author_email='FIXME',
    description='FIXME',
    long_description="FIXME",
    license='MIT',
    zip_safe=False,
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    install_requires=[
        'asgiref>=0.10',
        'twisted>=15.5',
        'autobahn>=0.12',
        'click>=6.6',
        'slackclient>=1.0.0',
        'pyopenssl>=16.0.0',
        'service_identity>=16.0.0',
    ],
    entry_points={'console_scripts': [
        'slackline = slackline.cli:cli',
    ]},
)
