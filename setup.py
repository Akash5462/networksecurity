'''
The setup.py file is an essential part of packaging and distributing python project . it is used by setuptools 
to define the configuration of your project , such as its metadata , dependencies , and more 
'''

from setuptools import find_packages,setup 
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirement_list:List[str]=[]

    try:
        with open('requirements.txt','r') as file :
            #reead line from the files 
            lines=file.readlines()
            ##process of each line 
            for line in lines :
                requirement=line.strip()
                ## ignore empty lines and -e . 
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError :
        print("requirements.txt file is not found ")

    return requirement_list 

setup(
    name="NetWorkSecurity",
    version="0.0.1",
    author="Akash Roy",
    author_email="akroy291@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)