from dotenv import load_dotenv
from src.infra.factory import Factory as FactoryLog

class Configuration:

    @staticmethod
    def read():
        if load_dotenv(dotenv_path = 'config.env'):  # Read only once, lazy.
            log = FactoryLog.build_logger()
            log.info("Arquivo de configurações encontrado. logger configurado!")