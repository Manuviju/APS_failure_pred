from setuptools import find_packages,setup
from typing import List


def get_requirements()-> List[str]:
    Hyphe_e_dot = "-e ."
    requirements_list:List[str]=[]
    with open('requirements.txt', 'r') as f:
        requirements_list = [line.rstrip() for line in f]
        if Hyphe_e_dot in requirements_list:
            requirements_list.remove(Hyphe_e_dot)
        
    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="avnish@ineuron.ai",
    packages = find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"],
)

