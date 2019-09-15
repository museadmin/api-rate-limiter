import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="apiqueue",
    version="0.1.0",
    description="Implement client side API rate limiting",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/museadmin/api-rate-limiter",
    author="Bradley  Atkins",
    author_email="bradley.atkinz@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    package_dir={'': 'apiqueue'},
    packages=find_packages("apiqueue", exclude=("tests",)),
    include_package_data=True,
)
