import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LI-pkg-gnouf1", # Replace with your own username
    version="1.0",
    author="gnouf1",
    author_email="jeuxforum26@gmail.com",
    description="Identify if a text is in french or english",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gnouf1/language-identifier",
    packages=setuptools.find_packages(),
    keywords = 'language english french identifier Identify offline',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
