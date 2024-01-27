import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if len(sys.argv) <= 1:
    print("""
Suggested setup.py parameters:

    * build
    * install
    * sdist  --formats=zip
    * sdist  # NOTE requires tar/gzip commands

    python -m pip install -e .

PyPi:

    python -m pip install setuptools twine
    twine upload dist/*
    ./setup.py  sdist ; twine upload dist/* --verbose

""")

setup(name='stache',  # TODO rename
      version='0.0.10',
      description='(Forked) Trimmed mustache logic-less templates',
      author='Linh-Nam Vu',
      author_email='github@l-vu.com',
      maintainer = "Chris Clark",
      url='https://github.com/clach04/stache',
      packages=['stache'],
      package_dir={'stache': '.'},
     )
