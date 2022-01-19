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
        # Github Private Repository - needs entry in `dependency_links`
        'senkalib'
    ],
    dependency_links=[
        'git+https://github.com/ca3-caaip/senkalib@32e01edccf32cb571f02da8989ef920c4c31e465#egg=senkalib'],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
