from setuptools import setup, find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Pratyush "
DESCRIPTION="ML Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mentioned in requirements.txt file

    Return: This function is going to return a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return  requirement_file.readlines().remove("-e .") # as we are using find_packages() which is equivalent to -e . hence removed -e .


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), # return all the folder name wherever it will find the __init__.py ['housing']
    install_requires=get_requirements_list() # to run this project what are the external libreries are required mentioned under requirements.txt file
                                             # -e . 

)

if __name__=="__main__":
    print(get_requirements_list())
