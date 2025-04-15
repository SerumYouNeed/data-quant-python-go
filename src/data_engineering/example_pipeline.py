# src/data_engineering/example_pipeline.py

from src.logger import get_logger

logger = get_logger(__name__)

def run_pipeline():
    logger.info("Starting example pipeline...")
    try:
        logger.debug("Loading data...")
        # error simulation
        1 / 0
    except Exception as e:
        logger.error("An error occurred", exc_info=True)

    logger.info("Pipeline finished.")

if __name__ == "__main__":
    run_pipeline()
