import pytest
from datetime import datetime
from cookie_analyzer.most_active_cookie import CookieLogProcessor, validate_date
import os

# Fixture for reusable CookieLogProcessor instance
@pytest.fixture
def processor():
    # Adjust the path according to your tests directory structure
    test_file_path = os.path.join(os.path.dirname(__file__), 'test_cookie_log.csv')
    return CookieLogProcessor(test_file_path)

def test_validate_date_valid():
    """Test date validation with a valid date."""
    assert validate_date("2018-12-09") == datetime(2018, 12, 9).date()

def test_validate_date_invalid():
    """Test date validation with an invalid date, expecting SystemExit."""
    with pytest.raises(SystemExit):
        validate_date("invalid-date")

def test_find_most_active_cookie(processor):
    """Test finding the most active cookie on a specific date with expected result."""
    target_date = datetime(2018, 12, 9).date()
    assert processor.find_most_active_cookie(target_date) == ['AtY0laUfhglK3lC7']

def test_find_most_active_cookie_no_data(processor):
    """Test finding the most active cookie on a date with no data."""
    target_date = datetime(2018, 12, 10).date()
    assert processor.find_most_active_cookie(target_date) == []

