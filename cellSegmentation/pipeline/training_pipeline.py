import sys, os
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.components.data_ingestion import DataIngestion
from cellSegmentation.components.data_validation import DataValidation


from cellSegmentation.entity.config_entity import (DataIngestionConfig,
                                                   DataValidationConfig)



from cellSegmentation.entity.artifacts_entity import (DataIngestionArtificat,
                                                      DataValidationArtifact)




class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()



    def start_data_ingestion(self)-> DataIngestionArtificat:
        try:
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            data_ingestion = DataIngestion(
                data_ingestion_config = self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Excited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e,sys)
        
    
    
    
    
    def start_data_validation(
            self, data_ingestion_artifact: DataIngestionArtificat
    ) -> DataValidationArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config = self.data_validation_config,
            )

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data valiation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact
        
        except Exception as e:
            raise AppException(e,sys)
    
    
    
    
    def run_pipeline(self) -> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(
                data_ingestion_artifact = data_ingestion_artifact
            )

        
        
        except Exception as e:
            raise AppException(e, sys)