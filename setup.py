import setuptools

from bojpy.version import __version__

with open("README.md", "r") as ld:
    long_description = ld.read()

setuptools.setup(
    name="bojpy",
    version=__version__,
    packages=["bojpy"],
    include_package_data=True,
    install_requires=["pandas", "requests", "beautifulsoup4"],
    url="https://github.com/philsv/bojpy",
    license="MIT",
    author="philsv",
    author_email="frphsv@gmail.com",
    description="Python Wrapper for the Bank of Japan (BOJ) Time-Series Data Search",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["boj", "bank of japan", "central bank", "statistical data"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "License :: OSI Approved :: MIT License",
    ],
)
