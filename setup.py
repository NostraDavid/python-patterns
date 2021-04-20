import pathlib

from setuptools import find_packages, setup

cwd = pathlib.Path.cwd()

with (cwd / "requirements" / "base.txt").open(mode="r") as requirements_file:
    requirements = requirements_file.read().splitlines()

about = {}
with (cwd / "src" / "python_patterns" / "__version__.py").open(mode="r") as about_file:
    exec(about_file.read(), about)

with (cwd / "README.md").open(mode="r") as readme_file:
    readme = readme_file.read()

setup(
    author=about["__author__"],
    description=about["__description__"],
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    long_description_content_type="text/markdown",
    long_description=readme,
    name=about["__title__"],
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    python_requires=">=3.6",
    url="https://thaumatorium.com/",
    version=about["__version__"],
    entry_points={
        "console_scripts": [
            "python_patterns=python_patterns.main:main",
        ],
    },
)
