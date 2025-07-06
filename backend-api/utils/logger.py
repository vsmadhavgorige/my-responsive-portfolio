from loguru import logger
import os

def init_logger():
    # Ensure log directory exists 
    log_dir = os.getenv("LOG_DIR")
    log_file_name = os.getenv("LOG_FILE_NAME")
    os.makedirs(log_dir, exist_ok=True)

    # Add logger with daily rotation at midnight
    logger.add(
        os.path.join(log_dir, log_file_name),
        rotation="1 day",             # Rotate daily at midnight
        retention="7 days",           # Keep logs for 7 days
        compression="zip",            # Compress old logs
        level="INFO",                 # Set log level
        backtrace=True,               # Helpful for debugging
        diagnose=True                 # Detailed stack trace
    )

log = logger