def read_file():
    try:
        with open("black.log", "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""  # or None

def get_file():
    file: str = read_file()
    print(file)

get_file()
