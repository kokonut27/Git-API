from setuptools import setup


with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "git_api",
  version = "1.0.2",
  description = "A GitHub API. Extracts data from GitHub into json style data.",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/JBYT27/GitAPI",
  author = "JBYT27",
  author_email = "beol0127@gmail.com",
  license = "MIT",
  packages=[''],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.6",
)
