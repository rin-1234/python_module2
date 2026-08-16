def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    print(f"Temperature is now {temp}°C")
    return temp


def test_temperature(temp_str: str) -> None:
    try:
        input_temperature(temp_str)
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    print("All tests completed - program didn't crash!")
