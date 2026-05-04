#   Python Libraries
from __future__ import annotations

import os, logging as log
from typing import Optional, Any, Dict


# Third-Party Libraries
import structlog
from serilog_python import setup_logging

class StandardLogger(object):
    def __init__(self, name: Optional[str] = None, dir:Optional[str] = None) -> None:

        self.name : str = name if name else self.__class__.__name__ 
        self.dir: Optional[str] = '.' + dir if dir else None
        self.log: log.Logger = log.getLogger(f"{self.name}") if self.name else log.getLogger()
        self.dictionary: Dict[int, int] = { 0: log.INFO, 1: log.DEBUG, 2: log.WARNING, 3: log.ERROR, 4: log.CRITICAL }

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
            self.log.critical(f"{self.name} - Console handler already initialized")
            return

        handler = log.StreamHandler()
        self.is_console = True
        self.setup_handler(handler)                                                                                     #type: ignore - StreamHandler is a valid type, but pylance doesn't recognize it.

    def file_handler(self) -> None:
        """
            *   Add a file handler to the logger
        """

        try:
            if self.is_file: raise ValueError(f"{self.name} - File handler already initialized")
            if not self.dir: raise ValueError("Directory for log files must be specified.")

            os.makedirs(self.dir, exist_ok=True)
            file_path = os.path.join(self.dir, self.name)

        except ValueError as e:
            print(f"Error: {e}")
            return

        handler = log.FileHandler(file_path)
        self.is_file = True

        self.setup_handler(handler)                                                                                     #type: ignore - FileHandler is a valid type, but pylance doesn't recognize it.
        self.log.info(f"{self.name} has been initialized.")

    def info(self, message: str) -> None: 
        
        level:int = 0
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.info(message)

    def error(self, message: str) -> None:
        level:int = 3
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.error(message)

    def warn(self, message: str) -> None:
        level:int = 2
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.warning(message)

    def debug(self, message: str) -> None:
        level:int = 1
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.debug(message)

    def critical(self, message: str) -> None:
        level:int = 4
        self.log.setLevel(self.dictionary.get(level, log.DEBUG))

        self.log.critical(message)

class StructLogger:
    def __init__(self, name: Optional[str] = None, dir: Optional[str] = None) -> None:
        self.name: str = name if name else self.__class__.__name__
        self.dir: Optional[str] = '.' + dir if dir else None
        
        # Configure structlog
        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.StackInfoRenderer(),
                structlog.processors.format_exc_info,
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.JSONRenderer()
            ],
            wrapper_class=structlog.make_filtering_bound_logger(20), # Default to INFO
            context_class=dict,
            logger_factory=structlog.PrintLoggerFactory(),
            cache_logger_on_first_use=True,
        )
        self.log = structlog.get_logger(self.name)
        self.is_file: bool = False
        self.is_console: bool = False

    def console_handler(self) -> None:
        """
        In structlog with PrintLoggerFactory, console is already the default destination.
        This method is kept for interface consistency.
        """
        self.is_console = True

    def file_handler(self) -> None:
        """
        Configure structlog to write to a file.
        """
        if self.is_file:
            return
        
        if not self.dir:
            return

        os.makedirs(self.dir, exist_ok=True)
        file_path = os.path.join(self.dir, self.name)
        
        # Redirect structlog to file
        structlog.configure(
            logger_factory=structlog.WriteLoggerFactory(file=open(file_path, "a", encoding="utf-8"))
        )
        self.is_file = True

    def info(self, message: str, **kwargs: Any) -> None:
        self.log.info(message, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        self.log.debug(message, **kwargs)

    def warn(self, message: str, **kwargs: Any) -> None:
        self.log.warning(message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        self.log.error(message, **kwargs)

    def critical(self, message: str, **kwargs: Any) -> None:
        self.log.critical(message, **kwargs)

class SeriLogger:
    def __init__(self, name: Optional[str] = None, dir: Optional[str] = None) -> None:
        self.name: str = name if name else self.__class__.__name__
        self.dir: Optional[str] = '.' + dir if dir else None
        
        # Initial setup (defaults to console)
        setup_logging(application_name=self.name)
        self.log = log.getLogger(self.name)
        
        self.is_file: bool = False
        self.is_console: bool = True

    def console_handler(self) -> None:
        """
        Console handler is active by default in serilog-python.
        """
        self.is_console = True

    def file_handler(self) -> None:
        """
        Configure file logging. serilog-python typically outputs to stdout/stderr 
        intended for container logs, but we can manually add a FileHandler.
        """
        if self.is_file:
            return
        
        if not self.dir:
            return

        os.makedirs(self.dir, exist_ok=True)
        file_path = os.path.join(self.dir, self.name)
        
        handler = log.FileHandler(file_path)
        formatter = log.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        handler.setFormatter(formatter)
        self.log.addHandler(handler)
        
        self.is_file = True

    def info(self, message: str, **kwargs: Any) -> None:
        self.log.info(message, extra=kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        self.log.debug(message, extra=kwargs)

    def warn(self, message: str, **kwargs: Any) -> None:
        self.log.warning(message, extra=kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        self.log.error(message, extra=kwargs)

    def critical(self, message: str, **kwargs: Any) -> None:
        self.log.critical(message, extra=kwargs)
