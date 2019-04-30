from setuptools import setup, find_packages

setup(
    name='greenberet',
    version='0.1',
    packages=['greenberet'],
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gb=greenberet.cli:cli
    ''',
)