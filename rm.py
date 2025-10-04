from pathlib import Path


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
    non_blank_lines = [line for line in lines if line]
    return non_blank_lines


def clean_lines(lines: list[str]) -> list[str]:
    error_lines = [line for line in lines if is_error_line(line)]
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


def delete_file(filename: str) -> None:
    Path(filename).unlink()


def delete_files(filenames: list[str]) -> bool:
    try:
        for filename in filenames:
            delete_file(filename)
        return True
    except Exception as e:
        print(e)
        return False


def run() -> None:
    lines = read_file_lines()
    errors = clean_lines(lines)
    filenames = get_filenames(errors)
    cleaned_filenames = clean_filenames(filenames)
    result = delete_files(cleaned_filenames)
    interpret_result(result)


def interpret_result(result):
    if result:
        print("files successfully deleted!")
    else:
        print("oops there was an issue")


def main() -> None:
    run()


main()
