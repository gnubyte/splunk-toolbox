import setuptools

# Needs twine, setuptools, wheel, tqdm pip installed first
# python setup.py bdist_wheel
# python -m twine upload dist/*

# grab readme and use as documentation dynamically
with open("README.md", "r") as fh:
    long_description = fh.read()

# grab requirements dynamically
with open('requirements.txt') as reqtext:
    requirements = reqtext.read().splitlines()

setuptools.setup(
    name="splunk-toolbox",
    version="1.2.0",
    scripts=['splunktoolbox'],
    author="Patrick Hastings",
    author_email="phastings@openmobo.com",
    description="A wrapper around the Splunk REST API endpoint",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gnubyte/splunk-toolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=requirements
)