def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        5 / 0
    elif operation_number == 2:
        open('hogehoge')
    elif operation_number == 3:
        "abc" + 123


def test_error_types(temp: int) -> None:
    try:
        garden_operations(temp)
    except ValueError as e:
        print(f"Caught ValueError error: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError error: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError error: {e}")
    except TypeError as e:
        print(f"Caught TypeError uuerror: {e}")
    except Exception as e:
        print(f"Caught error: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types(0)
    test_error_types(1)
    test_error_types(2)
    test_error_types(3)
    print("Operation completed successfully")
    print("All error types tested successfully!")
