from setuptools import setup, find_packages

setup(
    name="studio_tools",
    version="0.2.0",
    author="John Doe",
    description="A Studio tools which contains utitlities for studio",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
)