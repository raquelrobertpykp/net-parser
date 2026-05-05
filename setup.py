from setuptools import setup, find_packages

setup(
    name='net-parser',
    version='0.9.84',
    packages=find_packages(),
    install_requires=['requests>=2.28.0', 'click>=8.0'],
    entry_points={'console_scripts': ['net-parser=netparser:main']},
)
