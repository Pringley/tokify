from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "Tokify",
    version = "0.0.1",
    packages = find_packages(),
    
    author = "Ben Pringle",
    author_email = "ben.pringle@gmail.com",
    url = "http://github.com/Pringley/tokify",
    description = "Streaming tokenizer for Python",
    license = "MIT",
)
