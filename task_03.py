'''module provides functions for the task 3'''
import re
import sys
import pathlib as pl
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
        if pl.Path(file_path).is_file():
            with open(file_path, "r", encoding="utf-8") as file:
                return [parse_log_line(line.strip()) for line in file if line.strip()]
        raise FileNotFoundError
    except FileNotFoundError:
        return "Error. Log file is not found!"

def filter_logs_by_level(log_list: list, log_level: str) -> list:
    '''filter log by level'''
    return [log for log in log_list if log["level"].upper() == log_level.upper()]

def count_logs_by_level(log_list: list) -> dict:
    '''count log by level'''
    levels = [log['level'] for log in log_list]
    return dict(Counter(levels))

def display_log_counts(counts: dict):
    '''show count log by level. Use func count_logs_by_level to count'''
    print("Level of Log".center(17) +"|" + "Count".center(10))
    print("-----------------|----------")
    for log_level, count in counts.items():
        print(f"{log_level:<17}|{count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path to the log file.")
        sys.exit(1)
    try:
        log_file_path = sys.argv[1]
        logs = load_logs(log_file_path)
        log_counts = count_logs_by_level(logs)

        if len(sys.argv) == 3:
            level = sys.argv[2]
            filtered_logs = filter_logs_by_level(logs, level)
            print(f"Log details for level '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['datetime']} - {log['message']}")
        else:
            display_log_counts(log_counts)
    except Exception as e:
        print(e)
