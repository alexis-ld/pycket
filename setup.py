#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
setup(
    name='pycket',
    version="0.1",
    packages=find_packages(),
    author="Romain Zanchi, Alexis Le Dinh, Stephane Mombuleau",
    author_email="zanchi_r@epitech.eu",
    description="A simple python packet sniffer and manipulation tool",
    long_description=open('README.md').read(),
    install_requires=[
        "dpkt",
    ],
    include_package_data=True,
    url='https://github.com/alexis-ld/pycket',
    entry_points = {
        'gui_scripts': [
            'pycket = pycket.mainGUI:main',
        ],
    }
 )
