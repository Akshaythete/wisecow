#!/usr/bin/env python3

import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 90.0  # in percentage

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {usage}%")
    else:
        logging.info(f"CPU usage: {usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    usage = memory.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {usage}%")
    else:
        logging.info(f"Memory usage: {usage}%")

def check_disk():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f"Low disk space detected: {usage}% used")
    else:
        logging.info(f"Disk usage: {usage}%")

def log_running_processes():
    processes = [(p.info['pid'], p.info['name'], p.info['cpu_percent']) for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
    for pid, name, cpu in processes:
        logging.info(f"Process ID: {pid}, Name: {name}, CPU: {cpu}%")

if __name__ == "__main__":
    logging.info("System Health Monitoring Started")
    check_cpu()
    check_memory()
    check_disk()
    log_running_processes()
    logging.info("System Health Monitoring Completed")