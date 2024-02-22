from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as req:
    requirements = req.readlines()


setup(
    name="media-organizer",
    version="1.1.1",
    author="Waldirio",
    author_email="waldirio@gmail.com",
    description="This project will help you organize all of your medias, which means, basically, pictures and videos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/MultiMedia-Management/media-organizer",
    packages=find_packages(),
    python_requires=">=3.11",
    scripts=['bin/mo'],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)