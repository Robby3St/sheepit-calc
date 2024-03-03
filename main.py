from src.sheepit_calc import ask_for_calc_mode, make_calculation


if __name__ == '__main__':
    print("Welcome to the Sheepit Calculator!")
    calc_mode = ask_for_calc_mode()
    make_calculation(calc_mode)
