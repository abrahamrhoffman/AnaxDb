import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anax",
    version="1.0",
    author="Abraham Hoffman",
    author_email="abrahamrhoffman@gmail.com",
    description="An encrypted non-linear database based on Pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abrahamrhoffman/anaxdb",
    install_requires=[
        'pandas==0.23.4',
        'numpy==1.15.4',
        'pyarrow==0.11.1',
        'matplotlib==2.2.3',
        'seaborn==0.9.0',
        'pycryptodome==3.7.2',
        'pathlib==1.0.1',
        'minio==4.0.6'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
