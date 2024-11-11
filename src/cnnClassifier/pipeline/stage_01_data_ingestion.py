from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage "

class DataIngestionTrainingPipeline : 
    def __init__(self):
        pass
    def main(self): #if you call this function main the pipeline will start investigating data
        config = ConfigurationManager() 
        data_ingestion_config = config.get_data_ingestion_config() #initialize my config manager 
        data_ingestion = DataIngestion(config=data_ingestion_config) 
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__': #
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline() #initializing my data 
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e