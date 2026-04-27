from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# get version from __version__ variable in bas_ambulance/__init__.py
from bas_ambulance import __version__ as version

setup(
    name="bas_ambulance",
    version=version,
    description="Ambulance Service Management Module for ERPNext",
    author="BAS",
    author_email="info@bas.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
