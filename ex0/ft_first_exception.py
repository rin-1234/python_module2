def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    print(f"Temperature is now {temp}°C")
    return temp


def test_temperature() -> None:
    for temp_str in ("25", "abc"):
        try:
            input_temperature(temp_str)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print("All tests completed - program didn't crash!")
