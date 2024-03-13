#!/usr/bin/env python3

import argparse
from datetime import datetime
import logging
from sys import exit

# Constants
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
DATE_ONLY_FORMAT = "%Y-%m-%d"

# Configure logging
logging.basicConfig(level=logging.WARNING)

class CookieLogProcessor:
    """Processes cookie log files."""

    def __init__(self, file_path):
        """Initializes the processor with the path to a log file."""
        self.file_path = file_path
        self.cookie_logs = {}

    def load_logs(self, target_date):
        """Loads logs from a file for a specific date."""
        self.cookie_logs = {}  # Ensure cookie_logs is reset each time load_logs is called
        try:
            with open(self.file_path, 'r') as file:
                try:
                    next(file)  # Skip the header line, if it exists
                except StopIteration:
                    # The file is empty (or only contains a header), so there's nothing more to do
                    return
                for line in file:
                    cookie, timestamp = line.strip().split(',')
                    date = datetime.strptime(timestamp, DATE_FORMAT).date()
                    if date == target_date:
                        if cookie in self.cookie_logs:
                            self.cookie_logs[cookie] += 1
                        else:
                            self.cookie_logs[cookie] = 1
                    # laze load as data is sorted
                    elif date < target_date:
                        break
        except FileNotFoundError as e:
            logging.error(f"The file {self.file_path} was not found.")
            raise e


    def find_most_active_cookie(self):
        """Finds the most active cookie for a given date."""
        most_active = []
        max_occurrences = 0
        for cookie, count in self.cookie_logs.items():
            if count > max_occurrences:
                most_active = [cookie]
                max_occurrences = count
            elif count == max_occurrences:
                most_active.append(cookie)
        return most_active

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description='Find the most active cookie in a log file for a specific date.')
    parser.add_argument('file', type=str, help='The log file containing cookie data.')
    parser.add_argument('-d', '--date', required=True, type=str, help=f'Find the most active cookie for this date (\'YYYY-MM-DD\').')
    return parser.parse_args()

def validate_date(date_str):
    """Validates the date format."""
    try:
        return datetime.strptime(date_str, DATE_ONLY_FORMAT).date()
    except ValueError as e:
        logging.error("Error: Date must be in valid YYYY-MM-DD format.")
        raise e

def main():
    """Main function to execute script logic."""
    try:
        args = parse_arguments()
        target_date = validate_date(args.date)
        processor = CookieLogProcessor(args.file)
        processor.load_logs(target_date)
        most_active_cookies = processor.find_most_active_cookie()

        if most_active_cookies:
            for cookie in most_active_cookies:
                print(cookie)
        else:
            print("No data for the given date.")
    except Exception as e:
        logging.error(str(e))
        exit(1)

if __name__ == "__main__":
    main()
