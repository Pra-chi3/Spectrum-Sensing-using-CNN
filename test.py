import logging
import logging.handlers
from pathlib import Path


class LoggerSetup:
    """Simple logger setup class"""
    
    _logger = None  # Singleton instance
    
    @classmethod
    def setup_logger(
        cls,
        log_path: str = "logs/app.log",
        log_level: str = "INFO",
        max_bytes: int = 5000000,
        backup_count: int = 5
    ) -> logging.Logger:
        """
        Setup and configure logger with file and console handlers.
        
        Args:
            log_path: Path to log file
            log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            max_bytes: Maximum size of log file before rotation (default: 5MB)
            backup_count: Number of backup files to keep (default: 5)
            
        Returns:
            Configured logger instance
        """
        # Return existing logger if already configured
        if cls._logger is not None:
            return cls._logger
        
        # Create logger
        logger = logging.getLogger("LogAnalyzer")
        logger.setLevel(getattr(logging, log_level.upper()))
        
        # Clear existing handlers to avoid duplicates
        logger.handlers.clear()
        
        # Create formatter
        log_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s",
            datefmt="%d-%m-%Y %I:%M:%S %p"
        )
        
        # Ensure log directory exists
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        
        # File handler with rotation
        file_handler = logging.handlers.RotatingFileHandler(
            log_path,
            mode='a',
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        logger.addHandler(console_handler)
        
        cls._logger = logger
        return logger
    
    @classmethod
    def get_logger(cls) -> logging.Logger:
        """Get the configured logger instance"""
        if cls._logger is None:
            return cls.setup_logger()
        return cls._logger
