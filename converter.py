def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

def validate_temperature(value: float, scale: str) -> bool:
    if scale not in ("C", "F"):
        raise ValueError(f"Unknown scale: {scale}")
    if scale == "C" and value < -273.15:
        raise ValueError("Temperature below absolute zero (-273.15 C)")
    if scale == "F" and value < -459.67:
        raise ValueError("Temperature below absolute zero (-459.67 F)")
    return True
