from setuptools import setup
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

REPO_NAME = "Books-Recommendation-System"
AUTHOR_USER_NAME = "adishree"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit' , 'numpy' ]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small python package for ML app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="adishreejalgaonkar2022@kccemsr.edu.in",
    packages=[SRC_REPO],
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)