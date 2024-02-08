import logging
import os
from datetime import datetime

# create log directory
LOG_DIR = "logs"
LOG_DIR_PATH = os.path.join(os.getcwd(), LOG_DIR)

# Create log directory using os.makedirs
os.makedirs(LOG_DIR, exist_ok=True)

# Create logfile name
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}"
log_file_path = os.path.join(LOG_DIR, file_name)

# configure logging
logging.basicConfig(level=logging.INFO,
                    filename=log_file_path,
                    format="%(asctime)s %(levelname)s %(module)s ============>%(message)s",
                    datefmt= "%d-%m-%Y %H:%M")
                
# create object for logging
logger = logging.getLogger()