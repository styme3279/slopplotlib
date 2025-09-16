from setuptools import setup, find_packages

setup(
    name = 'slopplotlib-james',
    version  =  '0.1.0',
    packages = find_packages(),
    install_requires = [
        'matplotlib',
        'plotly'
    ],
    author = 'James Hindmarch',
    author_email = 'jameshindmarch02@gmail.com',
    description = 'Plotting for dummies',
    url = 'https://github.com/styme3279/slopplotlib',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)