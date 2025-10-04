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
    non_blank_lines = list(filter(None, lines))
    return non_blank_lines


def clean_lines(lines: list[str]) -> list[str]:
    error_lines = list(filter(is_error_line, lines))
    return error_lines


def is_error_line(line: str) -> bool:
    words = line.split()
    if len(words) == 0:
        return False
    if words[0] != "error:":
        return False
    return True


def get_filenames(errors: list[str]) -> list[str]:
    filenames = list(map(get_filename, errors))
    return filenames


def get_filename(error: str) -> str:
    words = error.split()
    filenames = list(filter(is_filename, words))
    if len(filenames) != 1:
        raise Exception("Expected exactly one filename")
    return filenames[0]


def is_filename(word: str) -> bool:
    leetcode_dir = "/Users/mike/Code/leetcode"
    return leetcode_dir in word


def clean_filenames(filenames: list[str]) -> list[str]:
    return [x.strip(":") for x in filenames]


def run() -> None:
    lines = read_file_lines()
    errors = clean_lines(lines)
    filenames = get_filenames(errors)
    cleaned_filenames = clean_filenames(filenames)
    print(cleaned_filenames)


def main() -> None:
    run()


main()
