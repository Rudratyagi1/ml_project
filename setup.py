from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

    # remove -e . if present
    if '-e .' in requirements:
        requirements.remove('-e .')

    return requirements


setup(
    name='ml_project',
    version='0.1.0',
    author='Rudra Tyagi',
    author_email='rudratyagi777@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project setup example',
)
