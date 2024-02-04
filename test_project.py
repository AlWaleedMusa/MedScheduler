import os
import pytest
from project import validate_time, calculate_next_pill, show_medicine

def test_validate_time():
    # Test valid time
    assert validate_time("12:30") == "12:30"
    assert validate_time("01:45") == "01:45"

    # Test invalid time
    assert validate_time("25:00") is None
    assert validate_time("abc") is None

def test_calculate_next_pill():
    # Test for a valid calculation
    assert calculate_next_pill("12:30", 8) == "20:30"

    # Test for edge case
    assert calculate_next_pill("23:45", 2) == "01:45"
    
def test_show_medicine(tmp_path, capsys):
    # Create a temporary CSV file
    csv_file = tmp_path / "temp.csv"

    # Write initial data
    with open(csv_file, "w") as file:
        file.write("Pill_Name,Starting_time,Next_pill,Dosing\n")
        file.write("Aspirin,08:00,16:00,8\n")
        file.write("Ibuprofen,14:30,22:30,8\n")

    # Call show_medicine function
    show_medicine(csv_file)

    # Capture the printed output
    captured = capsys.readouterr()

    # Ensure the correct data is displayed
    assert "Pill_Name" in captured.out
    assert "Aspirin" in captured.out
    assert "Ibuprofen" in captured.out
