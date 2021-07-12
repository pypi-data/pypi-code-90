import pathlib
from setuptools import setup, find_packages
import codecs
import os

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="MatrixBabou",
    version="0.0.9",
    description="This library is for linear algebra, Matrix analysis ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mohamedlaminebabou/BABOUMATH/",
    author="Babou Mohamed Lamine ",
    author_email="mohamedlaminebabou@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=['numba', 'numpy','pyccel','f2py',
    'sympy>=1.2',
    'termcolor',
    'textx>=1.6',
    'filelock'],
    keywords=['python', 'matrix', 'Matrix product', 'Matrix analysis'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

    

)
