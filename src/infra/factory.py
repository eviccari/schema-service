import logging

import os

class Factory:

    __log = None

    @staticmethod
    def build_logger() -> logging :
        if Factory.__log is None :
            logging.basicConfig(level=int(os.getenv('logLevel')), format='%(levelname)s - %(message)s')
            Factory.__log = logging
        return Factory.__log
