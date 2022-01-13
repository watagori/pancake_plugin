from setuptools import setup, find_packages
from glob import glob

setup(
    name='pancake_plugin',
    version='0.0.1',
    license='mit',
    description='plugin for pancake',

    author='ca3-caaip',
    author_email='',
    url='https://github.com/ca3-caaip/ca3-caaip',

    packages=find_packages('src'),
    package_dir={'': 'src'}
)