from setuptools import setup, find_packages

with open("README.md", "r") as input_file:
    long_description = input_file.read()

setup(
    name="gpugpu",
    version="1.0.0",
    description="gpugpu shows current statistics of GPUs and memory usage by running containers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonghwanhyeon/gpugpu",
    author="Jonghwan Hyeon",
    author_email="jonghwanhyeon93@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Home Automation",
    ],
    keywords=["gpu", "usage", "docker", "container"],
    packages=find_packages(),
    install_requires=["colored", "docker", "nvidia-ml-py3", "psutil"],
)
