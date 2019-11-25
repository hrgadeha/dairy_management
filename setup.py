# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dairy_management/__init__.py
from dairy_management import __version__ as version

setup(
	name='dairy_management',
	version=version,
	description='App for Dairy Management',
	author='Jamali Infocom',
	author_email='info',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
