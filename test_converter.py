import pytest
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, validate_temperature

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

def test_validate_temperature_valid():
    assert validate_temperature(25, "C") is True
    assert validate_temperature(77, "F") is True

def test_validate_temperature_invalid_scale():
    with pytest.raises(ValueError, match="Unknown scale"):
        validate_temperature(100, "K")

def test_validate_temperature_below_absolute_zero():
    with pytest.raises(ValueError, match="below absolute zero"):
        validate_temperature(-300, "C")
