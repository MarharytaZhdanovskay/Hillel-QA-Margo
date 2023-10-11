"""
HomeWork_23
Моніторингова система клєнта надсилає сигнал кожні 30 сек.
Засобами автоматизації проаналізуйте наданий нам лог в папці.
Змініть заготовку - файл hb_proces.py так? щоб там був аналіз правилності вимоги:
1. для кожного випадку де hertbeat більше 30 сек але менше 32 логувало варнінг в файл log_file.log
2. для кожного випадку де hertbeat більше рівно 32 логувало error в файлік log_file.log
"""


import re
import logging
from datetime import datetime, timedelta
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Створюємо обробник для запису в файл
file_handler = logging.FileHandler('log_file.log')
file_handler.setLevel(logging.DEBUG)

# Створюємо обробник для виводу в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Встановлюємо форматування
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


# Додаємо обробники до логгера
logger.addHandler(file_handler)
logger.addHandler(console_handler)


hblog_file = Path(__file__).parent / 'hblog.txt'
log_file = Path(__file__).parent / "log_file.log"

timestamp_pattern = r"(\d{2}:\d{2}:\d{2})"
previous_timestamp = None

with open(hblog_file, mode='r') as f:
    lines = f.readlines()

    for line in lines:
        match = re.search(timestamp_pattern, line)
        parts = line.split()
        if match:
            timestamp = match.group(1)
            current_timestamp = datetime.strptime(timestamp, "%H:%M:%S")

            if previous_timestamp is not None:
                time_difference = previous_timestamp - current_timestamp

                with open(log_file, mode="a") as log:
                    if timedelta(seconds=30) < time_difference < timedelta(seconds=32):
                        log.write(f"Warning: heartbeat = {time_difference.total_seconds()} sec\n")
                    elif timedelta(seconds=32) <= time_difference:
                        log.write(f"Error: heartbeat = {time_difference.total_seconds()} sec\n")

            previous_timestamp = current_timestamp
