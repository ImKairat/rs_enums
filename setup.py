"""
Setup configuration for the my_package project.
This module uses setuptools to package the application.
"""
from setuptools import setup, find_packages

setup(
    name="rs_enums",
    version="0.1.1-beta",
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache-2.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    )
