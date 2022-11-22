"""Utilitary functions
"""


def get_input(day: int) -> list[list[str]]:
    """File reading function for a given day

    Args:
        day (int): number of the day from 1 to 24

    Returns:
        list[list[str]]: the lines of the input file
    """
    filename = f"inputs/day{day}.txt"

    with open(filename) as file_stream:
        input_lines = file_stream.readlines()

    clean_input_lines = [input_line.replace("\n", "") for input_line in input_lines]
        
    return clean_input_lines
