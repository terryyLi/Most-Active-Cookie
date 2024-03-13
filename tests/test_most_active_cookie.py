import pytest
from datetime import datetime
from most_active_cookie import CookieLogProcessor, validate_date, parse_arguments
import os

@pytest.fixture
def processor():
    test_file_path = os.path.join(os.path.dirname(__file__), 'test_cookie_log.csv')
    return CookieLogProcessor(test_file_path)

def test_validate_date_valid():
    """Test date validation with a valid date."""
    assert validate_date("2018-12-09") == datetime(2018, 12, 9).date()

def test_validate_date_invalid():
    """Test date validation with an invalid date, expecting ValueError."""
    with pytest.raises(ValueError):
        validate_date("invalid-date")

def test_find_most_active_cookie_dec_9(processor):
    """Test finding the most active cookie on Dec 9, 2018, with expected result."""
    target_date = datetime(2018, 12, 9).date()
    processor.load_logs(target_date)
    assert processor.find_most_active_cookie() == ['AtY0laUfhglK3lC7']

def test_find_most_active_cookie_dec_8_with_tie(processor):
    """Test finding the most active cookie on Dec 8, 2018, with a tie."""
    target_date = datetime(2018, 12, 8).date()
    processor.load_logs(target_date)
    assert sorted(processor.find_most_active_cookie()) == sorted(['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG'])

def test_find_most_active_cookie_dec_10_no_data(processor):
    """Test finding the most active cookie on Dec 10, 2018, with no data."""
    target_date = datetime(2018, 12, 10).date()
    processor.load_logs(target_date)
    assert processor.find_most_active_cookie() == []

def test_parse_arguments_missing_file():
    """Test the argument parser for missing file argument."""
    with pytest.raises(SystemExit):
        parser = parse_arguments()
        parser.parse_args(['-d', '2018-12-09'])

def test_parse_arguments_missing_date():
    """Test the argument parser for missing date argument."""
    with pytest.raises(SystemExit):
        parser = parse_arguments()
        parser.parse_args(['cookie_log.csv'])

def test_file_not_found():
    """Test the response when a non-existent file is provided."""
    with pytest.raises(FileNotFoundError):
        CookieLogProcessor('non_existent_file.csv').load_logs(datetime.now().date())

def test_find_most_active_cookie_empty_file(processor):
    """Test finding the most active cookie in an empty file."""
    empty_file_path = os.path.join(os.path.dirname(__file__), 'test_empty_cookie_log.csv')
    processor = CookieLogProcessor(empty_file_path)
    target_date = datetime(2018, 12, 9).date()
    processor.load_logs(target_date)
    assert processor.find_most_active_cookie() == []
