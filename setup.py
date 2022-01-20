from setuptools import setup, find_packages
from glob import glob
from os.path import splitext
from os.path import basename

setup(
    name='pancake_plugin',
    version='0.0.3',
    license='mit',
    description='plugin for pancake',

    author='ca3-caaip',
    url='https://github.com/ca3-caaip/ca3-caaip',

    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')]    
)
