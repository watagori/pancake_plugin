from setuptools import setup, find_packages
from glob import glob

setup(
    name='pancake_plugin',
    version='0.0.1',
    license='mit',
    description='plugin for pancake',

    author='ca3-caaip',
    url='https://github.com/ca3-caaip/ca3-caaip',

    install_requires=[
        'senkalib'
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
