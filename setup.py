from setuptools import find_packages, setup
from typing import List

# -e . is mapped to setup.py
# It serves as an indication that setup.py file is there, and automatically the entire package will get made
HYPHEN_E_DOT= '-e .'

def get_requirements (file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()

        # \n also gets read so we replace it with blank
        [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements

setup (
name='EDA-Student-Performance',
version='0.0.1',
author='Abhinav',
packages=find_packages(), 
install_requires=get_requirements('requirements.txt')

)