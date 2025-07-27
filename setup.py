import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-To-End-Mushroom-with-MLFLOW"
AUTHOR_USER_NAME = "MannShrestha"
USER_NAME = "Mann Shrestha"
AUTHOR_EMAIL = "mannshrestha01@gmail.com"


setuptools.setup(
    name=USER_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)