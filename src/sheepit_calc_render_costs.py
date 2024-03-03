from src.sheepit_calc_helpers import str_to_number


def ask_for_frames_to_render() -> int:
    """
    Ask for the amount of frames to render
    :return: Returns the amount of frames to render as a number
    """
    raw = input("How many frames do you want to render: ")
    return str_to_number(raw)


def calculate_total_cost(total_time: float, point_price: float) -> int:
    """
    Calculate the total cost to render in sheepit points
    :param total_time: The total time to render
    :param point_price: The total time to render
    :return: The total cost to render
    """
    return round(total_time * point_price)
