import logging
import logging.handlers
from pathlib import Path


class LoggerSetup:
    """Logger setup class with instance methods"""
    
    def __init__(self, log_path: str, log_level: str = "INFO"):
        self.log_path = log_path
        self.log_level = log_level
        self.logger = None
    
    def setup_logger(self, max_bytes: int = 5000000, backup_count: int = 5) -> logging.Logger:
        """Setup and configure logger"""
        self.logger = logging.getLogger()
        self.logger.setLevel(getattr(logging, self.log_level.upper()))
        self.logger.handlers.clear()
        
        log_formatter = logging.Formatter(
            "%(asctime)s %(levelname)s %(message)s",
            datefmt="%d-%m-%Y %I:%M:%S %p"
        )
        
        Path(self.log_path).parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.handlers.RotatingFileHandler(
            self.log_path,
            mode='a',
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setFormatter(log_formatter)
        self.logger.addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        self.logger.addHandler(console_handler)
        
        return self.logger

# Usage
logger_setup = LoggerSetup(log_path="logs/app.log", log_level="INFO")
logger = logger_setup.setup_logger()
logger.info("Started")
