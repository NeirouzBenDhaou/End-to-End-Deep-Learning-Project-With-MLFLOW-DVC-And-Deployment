# End-to-End-Deep-Learning-Project-With-MLFLOW-DVC-And-Deployment> kidney/scripts/activateMLFLOW-DVC-And-Deployment

## Workflows

1.Update config.yaml
# database don't want to share with user in this project we don't have 
2.Update secrets.yaml [Optional] 
3.Update params.yaml
# we created config_entity we put in class dataingestionconfig 
4.Update the entity 
# we create class config manager in which 2 functions
5.Update the configuration manager in src config
# we create dataingestion file in which class dataingestion that fetch data from url and extract it 
6.Update the components
# we created file stage 01data ingestion contain class datain gestion training pipeline
7.Update the pipeline
# endpoint : recoit input and raise exception if needed
8.Update the main.py
# tracking your intern pipeline
9.Update the dvc.yaml
# create an other route
10.app.py
# How to run?
### STEPS:
Clone the repository
```bash 
https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
### STEP 01- Create a conda environment after opening the repository
```bash 
conda create -n cnncls python=3.8 -y
```
```bash
conda activate cnncls
```
### STEP 02- install the requirements
```bash
pip install -r requirements.txt


### Step 03- MLFLOW 
