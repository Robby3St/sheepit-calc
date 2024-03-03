from src.sheepit_calc_helpers import *
from src.sheepit_calc_render_costs import *
from src.sheepit_calc_time_for_points import *


def ask_for_calc_mode() -> int:
    """
    Ask for the mode to calculate
    :return: Returns the mode as a number
    """
    raw = input("What do you want to calculate? (1) Needed points to render a project, "
                "(2) The render time you get for the amount of points: ")
    return str_to_number(raw)


def make_calculation(mode: int):
    """
    Make the calculation based on the mode
    :param mode: The mode for calculation
    :return:
    """
    if mode == 1:
        calc_costs_for_render()
    elif mode == 2:
        calc_render_time_for_points()
    else:
        print("Invalid mode")
        raise ValueError("Invalid mode")


def calc_costs_for_render():
    """
    Calculates the costs to render a project
    :return:
    """
    frames = ask_for_frames_to_render()
    time_per_frame = ask_for_time_per_frame()
    total_time = calculate_total_time(frames, time_per_frame)
    point_price = ask_for_point_price()
    total_cost = calculate_total_cost(total_time, point_price)

    print_result_notifier()
    print(f"The price to render {format_great_number(frames)} frames in the total time "
          f"of {format_great_number(round(total_time))} render minutes is "
          f"{format_great_number(total_cost)} points.")


def calc_render_time_for_points():
    """
    Calculates the render time you get for a specific amount of points
    :return:
    """
    points = ask_for_points()
    point_price = ask_for_point_price()
    time_per_frame = ask_for_time_per_frame()
    render_time = calc_total_render_time_for_points(points, point_price, time_per_frame)

    print_result_notifier()
    print(f"The render time you get for {format_great_number(points)} points is "
          f"{format_great_number(round(render_time))} render minutes. "
          f"This are {format_minutes(round(render_time))}. You can get up to "
          f"{format_great_number(calc_frames_for_amount_of_points(points, point_price, time_per_frame))} "
          f"frames rendered.")


def print_result_notifier():
    print("The calculation is done. Have a nice day!")
    print(10 * '=', "Result", 10 * '=')
