"""When called, starts a new day by creating an empty .txt file for the input,
as well as an empty .py file for the code
"""


import os


def start_day():
    day_number = int(input("Which day is it ?\nDay : "))

    input_filename = f"inputs/day{day_number}.txt"
    code_filename = f"advent-of-code-2022/day{day_number}.py"

    if os.path.exists(input_filename) or os.path.exists(code_filename):
        raise SystemExit("This day has already been created...")

    with open(input_filename, "w"):
        print(f"You're gonna have to copy/paste the input from the website into the file {input_filename}...")

    with open(code_filename, "w") as code_file_stream:
        print(f"Creating code file with basic lines...")
        code_file_stream.write(open("data/base_code_file.txt").read().replace("DAYNUMBER", str(day_number)))

    print(f"Files {code_filename} & {input_filename} have been created !")


if __name__ == "__main__":
    start_day()
