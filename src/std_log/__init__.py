from .std_log import StandardLogger, StructLogger, SeriLogger

# Alias for backward compatibility
Logger = StandardLogger

__all__ = ["StandardLogger", "StructLogger", "SeriLogger", "Logger"]
