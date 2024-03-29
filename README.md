# Most Active Cookie Finder

The `most_active_cookie` script is a command-line tool designed to find the most active cookie in a given log file on a specified date.

## Description

Given a cookie log file in CSV format, this script will output the cookie(s) that appeared the most on a particular day. Unit tests are automated in git action.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/most-active-cookie.git
```

### Setup

Make the script executable if it's not:

```bash
chmod +x most_active_cookie
```

### Usage

To run the `most_active_cookie` script, use the following command:
```bash
./most_active_cookie <path_to_cookie_log.csv> -d <YYYY-MM-DD>
```

Here, `<path_to_cookie_log.csv>` should be replaced with the path to your cookie log file, and <YYYY-MM-DD> should be replaced with the date for which you want to find the most active cookie.

Example:
```bash
./most_active_cookie cookie_log.csv -d 2018-12-09
```

This will output the most active cookie(s) for December 9th, 2018, based on the data in `cookie_log.csv`.

### Exercise test suite
```bash
# Create a virtual environment (if not already created)
python3 -m venv venv

# Activate the virtual environment (for Unix/MacOS)
source venv/bin/activate

# Activate the virtual environment (for Windows)
venv\Scripts\activate.bat

# Install the required packages
pip install -r requirements.txt

# Run unit tests
pytest

# Deactivate virtual environment
deactivate
```
