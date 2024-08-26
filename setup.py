from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "CNNClassification"
VERSION = "0.0.1"
DESCRIPTION = "This is our Deep learning project used for classification purpose."
AUTHOR_NAME = "pramodkhavare"
AUTHOR_EMIL = "pramodkhavare2000@gmail.com"
REPO_NAME =  "Kidney-Disease-Classification-MLflow-DV"
REQUIREMENTS_FILE_NAME = "requirements.txt"


with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

HYPHEN_E_DOT = "-e ."

def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)

        return requriment_list

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMIL,
      long_description= LONG_DESCRIPTION ,
      url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
      project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
      },
      packages=find_packages(),
      install_requries = get_requirements_list()
     )
