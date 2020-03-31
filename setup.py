import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anax",
    version="1.1",
    author="Abraham Hoffman",
    author_email="abrahamrhoffman@gmail.com",
    description="An encrypted non-linear database based on Pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abrahamrhoffman/anaxdb",
    install_requires=[
        'pandas==1.0.3',
        'numpy==1.18.2',
        'pyarrow==0.16.0',
        'matplotlib==3.2.1',
        'seaborn==0.10.0',
        'pycryptodome==3.9.7',
        'pathlib==1.0.1',
        'minio==5.0.8'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
