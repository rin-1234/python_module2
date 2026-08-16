def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    if temp > 40:
        raise Exception(f"{temp} is too hot for plants (max 40°C)")
    elif temp < 0:
        raise Exception(f"{temp} is too cold for plants (min 0°C)")
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
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didn't crash!")
