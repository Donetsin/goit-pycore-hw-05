'''module provides functions for the task 3'''
import re
import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    '''parsing line of log file'''
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)"
    match = re.match(pattern, line)
    if match:
        return{"datetime":match.group(1), 'level': match.group(2), "message": match.group(3)}
    raise ValueError("log file format is incorect!")

def load_logs(file_path: str) -> list:
    '''load log file'''
    try:
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            return [parse_log_line(line.strip()) for line in file if line.lstrip()]
    except FileNotFoundError:
        return "Error. Log file is not found!"

def filter_logs_by_level(logs: list, level: str) -> list:
    '''filter log by level'''
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    '''count log by level'''
    levels = [log['level'] for log in logs]
    return dict(Counter(levels))

def display_log_counts(counts: dict):
    '''show count log by level. Use func count_logs_by_level to count'''
    print("Level of Log".center(17) +"|" + "Count".center(10))
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the log file.")
        sys.exit(1)

log_file_path = sys.argv[1]
logs = load_logs(log_file_path)
log_counts = count_logs_by_level(logs)

if len(sys.argv) == 3:
    level = sys.argv[2]
    filtered_logs = filter_logs_by_level(logs, level)
    print(f"Деталі логів для рівня '{level.upper()}':")
    for log in filtered_logs:
        print(f"{log['datetime']} - {log['message']}")
        print()

display_log_counts(log_counts)
