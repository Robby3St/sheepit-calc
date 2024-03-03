from src.sheepit_calc_helpers import str_to_number


def calc_total_render_time_for_points(points: int, point_price: float, time_per_frame: float) -> float:
    """
    Calculate the total render time you get for a specific amount of points
    :param points: The amount of points
    :param point_price: The price per render minute
    :param time_per_frame: The time per frame
    :return: The total render time you get for the amount of points
    """
    return points / point_price * time_per_frame


def ask_for_points() -> int:
    """
    Ask for the amount of points to render
    :return: Returns the amount of points to render as a number
    """
    raw = input("How many points do you have to render: ")
    return str_to_number(raw)


def minutes_in_hours(minutes: int) -> float:
    """
    Convert minutes to hours and minutes
    :param minutes: The amount of minutes
    :return: The amount of hours
    """
    return minutes // 60


def minutes_in_days(minutes: int) -> float:
    """
    Convert minutes to days and minutes
    :param minutes: The amount of minutes
    :return: The amount of days
    """
    return minutes // 1440


def format_minutes(minutes: int) -> str:
    """
    Format minutes to a string
    :param minutes: The amount of minutes
    :return: The formatted string
    """
    days = minutes_in_days(minutes)
    hours = minutes_in_hours(minutes % 1440)
    return f"{int(days)} days, {int(hours)} hours and {minutes % 60} minutes"


def calc_frames_for_amount_of_points(points: int, point_price: float, time_per_frame: float) -> int:
    """
    Calculate the amount of frames you can render for a specific amount of points
    :param points: The amount of points
    :param point_price: The price per render minute
    :param time_per_frame: The time per frame
    :return: The amount of frames you can render for the amount of points
    """
    return int(points / point_price / time_per_frame)
