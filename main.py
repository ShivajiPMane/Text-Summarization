from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger


STAGE_NAME = "Data Ingestion "
try:
    logger.info(f'>>>>>> stage{STAGE_NAME} started <<<<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx================================x")
except Exception as e:
    logger.exception(e)
    raise e