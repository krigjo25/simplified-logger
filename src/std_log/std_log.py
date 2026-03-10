#   Python Libraries
from __future__ import annotations
import os, logging as log


class Logger(object):
    """
        Standard Logger to handle application logging using logging module.
        @param name: str - Name of the logger, default is the class name
        @param dir: str - Directory to save log files, default is '.log'

        *   The logger supports both console and file handlers, which can be initialized separately.
        *   The logger provides methods for logging messages at different levels: info, error, warning, debug, and critical.
        *   The logger ensures that handlers are not initialized multiple times, and logs a warning if an attempt is made to reinitialize a handler.
    """
    def __init__(self, name:str, dir:str):
        """
            *   This constructor sets up the logger with the specified name and
            directory for log files. It also initializes flags to track whether file
            and console handlers have been set up.
            *   param dir: str - default: '.log'
            *   param name: str - default: Class name
            
        """

        self.name = name
        self.dir: str = '.' + dir
        self.log = log.getLogger(f"{self.name}")
        self.dictionary = { 0: log.INFO, 1: log.DEBUG, 2: log.WARNING, 3: log.ERROR, 4: log.CRITICAL }

        #   Initialize the Flags
        self.is_file: bool = False
        self.is_console: bool = False

    def setup_handler(self, handler: log.FileHandler | log.StreamHandler) -> None:                                              #type: ignore - FileHandler and StreamHandler are valid types, but pylance doesn't recognize them.
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

    def file_handler(self) -> None:
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

    def info(self, message: str) -> None: 
        """
            This method logs an info message. It sets the log level to INFO before
            logging the message.
             *   param message: str - The message to log
        """
        level:int = 0
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.info(message)

    def error(self, message: str) -> None:
        """
            This method logs an error message. It sets the log level to ERROR before
            logging the message.
             *   param message: str - The message to log
        """
        level:int = 3
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.error(message)

    def warn(self, message: str) -> None:
        """
            This method logs a warning message. It sets the log level to WARNING before
            logging the message.
             *   param message: str - The message to log
        """
        level:int = 2
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.warning(message)

    def debug(self, message: str) -> None:
        """
            This method logs a debug message. It sets the log level to DEBUG before
            logging the message.
             *   param message: str - The message to log
        """
        level:int = 1
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.debug(message)

    def critical(self, message: str) -> None:
        """
            This method logs a critical message. It sets the log level to CRITICAL before
            logging the message.
             *   param message: str - The message to log
        """
        level:int = 4
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.critical(message)