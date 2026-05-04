# Project Architecture

## Overview
`simplified-logger` is a lightweight Python library that acts as a wrapper around the standard `logging` module. Its primary goal is to simplify the initialization and use of logging in Python applications by providing a pre-configured, object-oriented interface.

## Architecture Diagram
Below is a visualization of how the components interact:

![Architecture Diagram](./architecture.drawio)

*Note: The `.drawio` file can be opened and edited using [diagrams.net](https://app.diagrams.net/).*

## Core Components

### `Logger` Class
The central component of the library is the `Logger` class, defined in `src/std_log/std_log.py`. It manages:
- **Initialization:** Setting up a named logger instance.
- **Handler Configuration:** Managing both console and file output.
- **Level Mapping:** A dictionary-based mapping for simplified log levels.

## Key Mechanisms

### 1. Handler Management & Duplicate Prevention
To prevent redundant logs, the `Logger` class uses boolean flags (`is_file`, `is_console`) to track if a handler has already been added. If a user attempts to call `console_handler()` or `file_handler()` multiple times, the class either logs a critical message or raises an error to ensure only one instance of each handler exists.

### 2. Dynamic Log Levels
Unlike traditional logging patterns where the level is set once globally, `simplified-logger` dynamically sets the logger's level just before emitting a message. For example, calling `logger.error("message")` sets the level to `ERROR` and then logs the message. This ensures the message is always captured regardless of the previous state, although it deviates from standard threshold-based logging.

### 3. Automatic Directory Creation
When a file handler is initialized, the library automatically creates the target log directory (prefixed with a dot, e.g., `.logs/`) using `os.makedirs(exist_ok=True)`.

## Project Layout

```text
simplified-logger/
├── docs/
│   ├── architecture.md       # This document
│   └── architecture.drawio   # Diagram source
├── src/
│   └── std_log/
│       ├── __init__.py
│       ├── std_log.py        # Core implementation
│       └── std_log.pyi       # Type stubs
├── pyproject.toml            # Build configuration
└── README.md                 # Usage instructions
```

## Dependencies
- **Python 3.10+** (standard library only).
- No external runtime dependencies.
