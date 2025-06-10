from setuptools import setup, find_packages

setup(
    name="fprint",
    version="0.1.0",
    description="A printable console formatter with indent, color, width and alignment support",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="sleepingHimazin",
    url="https://github.com/sleepingHimazin/fprint",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "colorama",
        "wcwidth",
        "termcolor"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    license="MIT",
)
