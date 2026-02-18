import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/audit.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def audit(action, payload):
    logging.info(f"{action} | {payload}")
