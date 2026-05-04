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
pip install simplified-logging
```
Or simply download the file and place it in your project directory.

## Usage

### Standard Logging (Zero-Dependency)
The `StandardLogger` (aliased as `Logger` for backward compatibility) uses Python's built-in `logging` module.

```python
from std_log import StandardLogger

logger = StandardLogger(name="app.log", dir="logs")
logger.console_handler()
logger.file_handler()

logger.info("Application started")
```

### Structured Logging (JSON)
The `StructLogger` uses `structlog` to output machine-readable JSON logs, perfect for cloud log aggregators.

```python
from std_log import StructLogger

logger = StructLogger(name="app.json", dir="logs")
logger.info("user_login", user_id=123, ip="1.2.3.4")
```

### Serilog-Style Logging
The `SeriLogger` uses `serilog-python` for a modern, structured logging experience inspired by .NET's Serilog.

```python
from std_log import SeriLogger

logger = SeriLogger(name="serilog")
logger.info("Process completed", duration_ms=450, status="success")
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
├── .git/
├── .github/
├── .vscode/
├── LICENCE
├── README.md
├── pyproject.toml
└── src/
    └── std_log/
        ├── __init__.py
        ├── std_log.py
        └── std_log.pyi
```

## License
[Licence](./licence)

## Author
krigjo25 - krigjo25@gmail.com

## Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.
