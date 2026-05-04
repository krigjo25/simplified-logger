# Project Architecture

## Overview
`simplified-logger` is a lightweight Python library that acts as a wrapper around the standard `logging` module. Its primary goal is to simplify the initialization and use of logging in Python applications by providing a pre-configured, object-oriented interface.

## Architecture Diagram
Below is a visualization of how the components interact:

![Architecture Diagram](./architecture.drawio)

*Note: The `.drawio` file can be opened and edited using [diagrams.net](https://app.diagrams.net/).*

## Core Components

The library provides three distinct logger classes within `src/std_log/std_log.py`, each catering to different logging needs:

### 1. `StandardLogger` (Alias: `Logger`)
The classic wrapper around Python's standard `logging` module. It is zero-dependency and ideal for simple scripts and applications that need standard console and file output.

### 2. `StructLogger`
A wrapper around the `structlog` library. It is designed for structured logging, emitting logs in JSON format by default. This is ideal for modern cloud environments and log aggregation tools (e.g., ELK stack, Datadog).

### 3. `SeriLogger`
A wrapper around `serilog-python`, inspired by the popular .NET Serilog library. It supports structured logging with a focus on application-wide setup and compatibility with Serilog-based sinks.

## Key Mechanisms

### 1. Handler Management & Duplicate Prevention
Each logger class manages its own handlers. The `StandardLogger` uses boolean flags (`is_file`, `is_console`) to track initialization and prevent redundant handler attachment.

### 2. Back-end Specific Implementations
- **Standard:** Dynamically sets log levels on each call for maximum flexibility.
- **Structured:** Leverages `structlog` pipelines for high-performance JSON rendering.
- **Serilog:** Uses `setup_logging` from `serilog-python` to configure a standardized structured output.

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
