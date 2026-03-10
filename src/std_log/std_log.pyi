from typing import Optional


class Logger:
    """
        Standard Logger to handle application logging using logging module.
        @param name: Optional[str] - Name of the logger, default is the class name
        @param dir: Optional[str] - Directory to save log files, default is 'None' (no file logging)


        *   The logger supports both console and file handlers, which can be initialized separately.
        *   The logger provides methods for logging messages at different levels: info, error, warning, debug, and critical.
        *   The logger ensures that handlers are not initialized multiple times, and logs a warning if an attempt is made to reinitialize a handler.
    """
    def __init__(self, name: Optional[str] = None, dir: Optional[str] = None) -> None:
        """
            *   This constructor sets up the logger with the specified name and
            directory for log files. It also initializes flags to track whether file
            and console handlers have been set up.
            *   param dir: Optional[str] - default: None (no file logging)
            *   param name: str - default: Class name
        """
        ...

    def console_handler(self) -> None:
        """
            *   Add a console handler to the logger
        """
        ...
    
    def file_handler(self) -> None:
        """
            *   Add a file handler to the logger
        """
        ...

    def info(self, msg: str) -> None:
        """
            This method logs an info message. It sets the log level to INFO before
            logging the message.
             *   param message: str - The message to log
        """
        ...
    def error(self, msg: str) -> None:
        """
            This method logs an error message. It sets the log level to ERROR before
            logging the message.
             *   param message: str - The message to log
        """
        ...
    def warn(self, msg: str) -> None:
        """
            This method logs a warning message. It sets the log level to WARNING before
            logging the message.
             *   param message: str - The message to log
        """
        ...

    def debug(self, msg: str) -> None:
        """
            This method logs a debug message. It sets the log level to DEBUG before
            logging the message.
             *   param message: str - The message to log
        """
        ...

    def critical(self, msg: str) -> None:
        """
            This method logs a critical message. It sets the log level to CRITICAL before
            logging the message.
             *   param message: str - The message to log
        """
        ...