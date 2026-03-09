# Simplified Logger
A lightweight Python logging wrapper that simplifies the use of Python's standard logging module. This library provides an easy-to-use interface for logging to both console and files with minimal configuration.

## Features
-  **Simple API**: Clean and intuitive methods for all log levels
-  **File & Console Logging**: Support for both file and console handlers
-  **Formatted Output**: Pre-configured formatting with timestamps and log levels
-  **Auto Directory Creation**: Automatically creates log directories if they don't exist
-  **Duplicate Prevention**: Built-in checks to prevent duplicate handler initialization
-  **Multiple Log Levels**: Support for INFO, DEBUG, WARNING, ERROR, and CRITICAL levels

## Installation
Clone the repository or copy the `lib/standard-logger.py` file to your project:

```bash
pip install simplified-logger
```
Or simply download the file and place it in your project directory.

## Usage

### Basic Example

```python
from lib.standard_logger import Logger

# Initialize the logger
logger = Logger(name="app.log", dir="logs")

# Add console handler (outputs to terminal)
logger.console_handler()

# Add file handler (writes to file)
logger.file_handler()

# Log messages at different levels
logger.info("Application started successfully")
logger.debug("Debugging information")
logger.warn("This is a warning message")
logger.error("An error occurred")
logger.critical("Critical system failure")
```

### Console-Only Logging

```python
from lib.standard_logger import Logger

logger = Logger(name="console.log", dir="logs")
logger.console_handler()

logger.info("This will only appear in the console")
```

### File-Only Logging

```python
from lib.standard_logger import Logger

logger = Logger(name="app.log", dir="logs")
logger.file_handler()

logger.info("This will only be written to .logs/app.log")
```

### Custom Log Directory

```python
from lib.standard_logger import Logger

# Logs will be stored in .my-logs/application.log
logger = Logger(name="application.log", dir="my-logs")
logger.file_handler()
```

## API Reference

### Logger Class

#### `__init__(name: str, dir: str)`

Initialize a new logger instance.

- **name**: Name of the log file (e.g., "app.log")
- **dir**: Directory name where logs will be stored (prefix with '.' automatically added)

#### `console_handler() -> None`
Adds a console handler to output logs to the terminal/console.

#### `file_handler() -> None`
Adds a file handler to write logs to a file. Creates the directory if it doesn't exist.

#### `info(message: str)`
Logs an informational message (INFO level).

#### `debug(message: str)`
Logs a debug message (DEBUG level). Useful for detailed diagnostic information.

#### `warn(message: str)`
Logs a warning message (WARNING level).

#### `error(message: str)`
Logs an error message (ERROR level).

#### `critical(message: str)`
Logs a critical message (CRITICAL level). For severe errors that may cause application failure.

## Log Format
The logger uses the following format for all messages:

```
%(asctime)s - %(levelname)-8s - %(name)s - %(message)s
```

Example output:
```
2026-03-09 10:30:45,123 - INFO     - app.log - Application started successfully
2026-03-09 10:30:46,456 - WARNING  - app.log - This is a warning message
2026-03-09 10:30:47,789 - ERROR    - app.log - An error occurred
```

## Requirements

- Python 3.7+
- No external dependencies (uses standard library only)

## Project Structure

```
simplified-logger/
├── README.md
└── lib/
    └── standard-logger.py
```

## License
[Licence](./licence)

## Author
krigjo25 - krigjo25@gmail.com

## Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.
