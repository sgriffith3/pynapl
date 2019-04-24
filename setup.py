#!/usr/bin/env python3
# setup
import setuptools

with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="pynapl",
    version="0.0.6",
    author="Sam Griffith",
    author_email="samgriffith3@gmail.com",
    description="Python Native Automation Package Library",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/sgriffith3/pynapl",
    packages=['pynapl'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


