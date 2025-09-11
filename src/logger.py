import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.log"


LOGS_DIR = os.path.join(os.getcwd(), "logs")  # folder for logs

os.makedirs(LOGS_DIR, exist_ok=True)  # make folder if not exists

LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)  # full file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
)

