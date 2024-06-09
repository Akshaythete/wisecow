#!/usr/bin/env python3

import re
from collections import defaultdict, Counter
import sys

# Configurable variables
LOG_FILE = "log_analyzer.log"  # Path to the web server log file

# Regular expression for Common Log Format (CLF)
log_pattern = re.compile(
    r'(?P<ip>[\d.]+) - - \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\d+|-)')

# Counters for analysis
status_counter = Counter()
page_counter = Counter()
ip_counter = Counter()

# Function to parse log file
def parse_log_file(log_file):
    with open(log_file, "r") as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                data = match.groupdict()
                ip = data["ip"]
                request = data["request"].split()[1]
                status = data["status"]

                # Update counters
                status_counter[status] += 1
                page_counter[request] += 1
                ip_counter[ip] += 1

# Function to print summary report
def print_summary():
    print("\nSummary Report")
    print("==================\n")
    
    # Number of 404 errors
    print("Number of 404 errors:")
    print(status_counter["404"], "\n")
    
    # Most requested pages
    print("Most requested pages:")
    for page, count in page_counter.most_common(10):
        print(f"{page}: {count}")
    print()
    
    # IP addresses with the most requests
    print("IP addresses with the most requests:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count}")
    print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        LOG_FILE = sys.argv[1]  # Accept log file path as a command-line argument
    
    parse_log_file(LOG_FILE)
    print_summary()
