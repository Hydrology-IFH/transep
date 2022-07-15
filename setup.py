from setuptools import setup, find_packages
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(here)
import versioneer  # noqa: E402

cmdclass = versioneer.get_cmdclass()

with open(os.path.join(here, "requirements.txt"), encoding="utf-8") as f:
    REQUIREMENTS = f.read().strip().split('\n')

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

CLASSIFIERS = """
Development Status :: 4 - Beta
Intended Audience :: Science/Research
License :: OSI Approved :: MIT License
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: Implementation :: CPython
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

setup(
    name='transep',
    version=versioneer.get_version(),
    cmdclass=cmdclass,
    license='MIT',
    description='Transfer function hydrograph separation model (TRANSEP)',
    long_description=long_description,
    url="https://transep.readthedocs.io",
    author='Robin Schwemmle',
    author_email='robin.schwemmle@hydrology.uni-freiburg.de',
    python_requires=">=3.7",
    install_requires=REQUIREMENTS,
    test_require=['pytest'],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[c for c in CLASSIFIERS.split("\n") if c],
    zip_safe=False
)
