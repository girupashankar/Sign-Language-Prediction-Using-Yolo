import os 
import logging

logging.basicConfig(level=logging.INFO, format=f'%(asctime)s - %(name)s - %(message)s')

project_name="Sign-Language-Prediction-Using-Yolo"

list_of_files = [
    ".github/workflows/ci.yml",
    "data/.gitkeep",
    "docs/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/commponents/__init__.py",
    f"src/{project_name}/commponents/data_ingestion.py",
    f"src/{project_name}/commponents/data_validation.py",
    f"src/{project_name}/commponents/model_trainer.py",
    f"src/{project_name}/commponents/model_pusher.py",
    f"src/{project_name}/configuration/s3_operations.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/constant/__init__.py",
    f"src/{project_name}/constant/training_pipeline/__init__.py",
    f"src/{project_name}/constant/application.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/artifacts_entity.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",    
]

for filepath in list_of_files:
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the {filename}.")

    if(not os.path.exists(filename)) or  (os.path.getsize(filename)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file : {filename}")
    else:
        logging.debug(f"File {filename} already exists.")