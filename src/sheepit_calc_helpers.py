def ask_for_time_per_frame() -> float:
    """
    Ask for the max render time limit per frame
    :return: Returns the time per frame as a number
    """
    raw = input("What is the max render time limit per frame (default is 20): ")
    if raw == "":
        return 20.0
    return str_to_float(raw)


def calculate_total_time(frames: int, time_per_frame: float) -> float:
    """
    Calculate the total time to render
    :param frames: The amount of frames to render
    :param time_per_frame: The time per frame
    :return: The total time to render
    """
    return frames * time_per_frame


def ask_for_point_price() -> float:
    """
    Ask for the points per render minute
    :return: The price per render minute as a float
    """
    raw = input("Enter the price per render minute (default is 9.6): ")
    if raw == "":
        return 9.6
    return str_to_float(raw)


def str_to_number(string: str) -> int:
    """
    Convert a string to a number
    :param string: The string to convert
    :return: The number
    """
    try:
        return int(string)
    except ValueError:
        print("The value you entered is not a number")
        raise ValueError("The value you entered is not a number")


def str_to_float(string: str) -> float:
    """
    Convert a string to a float
    :param string: The string to convert
    :return: The float
    """
    try:
        return float(string)
    except ValueError:
        print("The value you entered is not a number")
        raise ValueError("The value you entered is not a number")


def format_great_number(number: int) -> str:
    """
    Format a number to a string with dots as thousands separator
    :param number: The number to format
    :return: The formatted number
    """
    return f"{number:,}".replace(",", ".")
