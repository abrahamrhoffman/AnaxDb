import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anaxdb",
    version="0.9.3",
    author="Abraham Hoffman",
    author_email="abrahamrhoffman@gmail.com",
    description="An encrypted non-linear database based on Pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abrahamrhoffman/anaxdb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
