"""Setup script for Terminal Fortune Cookie."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8') if (this_directory / "README.md").exists() else ""

setup(
    name="terminal-fortune-cookie",
    version="0.1.0",
    description="Delightful developer fortunes and ASCII art for your terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="",
    author_email="y.zichen@wustl.edu",
    url="https://github.com/ZichenYuan/terminal-fortune-cookie",
    packages=find_packages(),
    package_data={
        "fortune_cookie": ["data/*.json"],
    },
    include_package_data=True,
    install_requires=[
        "rich>=13.0.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "fortune-cookie=fortune_cookie.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    keywords="terminal fortune cookie developer ascii art motivation",
)