#   Python Libraries
from __future__ import annotations
import os, logging as log


class Logger(object):
    """
        Standard Logger to handle application logging using logging module.
    """
    def __init__(self, name:str, dir:str):
        """
            *   Initialize the logger
            *   Set the logging level based on the provided level
            *   Set the logging format
            *   Set the logging handler
            *   param dir: str - default: '.log'
            *   param name: str - default: Class name
            *   param level: int - default: logging.DEBUG
        """

        self.name = name
        self.dir: str = '.' + dir
        self.log = log.getLogger(f"{self.name}")
        self.dictionary = { 0: log.INFO, 1: log.DEBUG, 2: log.WARNING, 3: log.ERROR, 4: log.CRITICAL }

        #   Initialize the Flags
        self.is_file: bool = False
        self.is_console: bool = False

    def setup_handler(self, handler: log.FileHandler | log.StreamHandler):                                              #type: ignore - FileHandler and StreamHandler are valid types, but pylance doesn't recognize them.
        """
            *   Setup the Log handler
            *   param handler:[log.FileHandler, log.StreamHandler]
        """

        #   Initializing the formatter
        formatter = log.Formatter('%(asctime)s - %(levelname)-8s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)                                                                                    #type: ignore - addHandler is a valid method, but pylance doesn't recognize it.

    def console_handler(self) -> None:
        """
            *   Add a console handler to the logger
        """
        if self.is_console:
            self.log.warning(f"{self.name} - Console handler already initialized")
            return

        handler = log.StreamHandler()
        self.is_console = True
        self.setup_handler(handler)                                                                                     #type: ignore - StreamHandler is a valid type, but pylance doesn't recognize it.
        self.log.info(f"{self.name} has been initialized.")

    def file_handler(self):
        """
            *   Add a file handler to the logger
        """

        if self.is_file:
            self.log.warning(f"{self.name} - File handler already initialized")
            return

            #   Initializing the handler

        if self.dir:
            os.makedirs(self.dir,exist_ok=True)
            file_path = os.path.join(self.dir, self.name)

        else: file_path = self.name

        handler = log.FileHandler(file_path)
        self.is_file = True

        self.setup_handler(handler)                                                                                     #type: ignore - FileHandler is a valid type, but pylance doesn't recognize it.
        self.log.info(f"{self.name} has been initialized.")

    def info(self, message: str): 
        level:int = 0
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.info(message)

    def error(self, message: str):
        level:int = 3
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.error(message)

    def warn(self, message: str):
        level:int = 2
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.warning(message)

    def debug(self, message: str):
        level:int = 1
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.debug(message)

    def critical(self, message: str):
        level:int = 4
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.critical(message)