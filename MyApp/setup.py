from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "GITAPI",
  version = "0.0.1",
  description = "Github API. A module",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "#Github or Website. This parameter isn't needed.",
  author = "JBYT27",
  author_email = "Your email",#add email
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT",
  packages=['GITAPI'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)