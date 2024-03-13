#!/usr/bin/env python3

import argparse
from collections import defaultdict, Counter
from datetime import datetime

class CookieLogProcessor:
    """Processes cookie log files."""
    
    def __init__(self, file_path):
        """Initializes the processor with the path to a log file."""
        self.file_path = file_path
        self.cookie_logs = self._load_logs()

    def _load_logs(self):
        """Loads logs from a file, skipping the header and handling parsing errors."""
        logs = defaultdict(list)
        try:
            with open(self.file_path, 'r') as file:
                next(file)  # Skip the header line
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        cookie, timestamp = parts
                        try:
                            date = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S%z").date()
                            logs[date].append(cookie)
                        except ValueError:
                            print(f"Warning: Skipping line due to parsing error: {line.strip()}")
                    else:
                        print(f"Warning: Skipping malformed line: {line.strip()}")
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            exit(1)
        return logs

    def find_most_active_cookie(self, target_date):
        """Finds the most active cookie for a given date."""
        cookies = Counter(self.cookie_logs[target_date])
        if cookies:
            max_occurrences = max(cookies.values())
            return [cookie for cookie, count in cookies.items() if count == max_occurrences]
        return []

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description='Process cookie logs.')
    parser.add_argument('file', type=str, help='The log file containing cookie data.')
    parser.add_argument('-d', '--date', required=True, type=str, help='Find the most active cookie for this date (YYYY-MM-DD).')
    return parser.parse_args()

def validate_date(date_str):
    """Validates the date format."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Date must be in YYYY-MM-DD format.")
        exit(1)

def main():
    """Main function to execute script logic."""
    args = parse_arguments()
    target_date = validate_date(args.date)
    processor = CookieLogProcessor(args.file)
    most_active_cookies = processor.find_most_active_cookie(target_date)

    if most_active_cookies:
        for cookie in most_active_cookies:
            print(cookie)
    else:
        print("No data for the given date.")

if __name__ == "__main__":
    main()
