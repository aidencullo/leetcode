def read_file() -> str:
    filename = "black.log"
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def read_file_lines() -> list[str]:
    file = read_file()
    lines = file.splitlines()
    return lines


result = read_file_lines()
print(result)
