import os 
from pathlib import Path
import logging # because i want to log all the information during the run time.

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "textsummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging//__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt", 
    "setup.py",
    "research/trails.ipynb"  

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # separate folder like entity and files like __init__.py

    if filedir != "":  # folder should not be empty, hence checking the conditon whether it is empty or not. folder should contain init file.
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):  # if the file doesnt exist or size of the directory is zero then open or create and empty file in write mode 
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")