from src.CNNClassifier.pipeline.training_pipeline import TrainPipeline 
from src.CNNClassifier.config.configuration import ConfigurationManager
from src.CNNClassifier.logger import logging 
def main():
    try:
        pipeline = TrainPipeline(config=ConfigurationManager())
        print(12)
        pipeline.run()

    except Exception as e:
        logging.error(f"{e}")


if __name__ == "__main__":
    main()