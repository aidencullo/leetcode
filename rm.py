from pathlib import Path

BLACK_LOG = Path("black.log")
LEETCODE_DIR = "/Users/mike/Code/leetcode"


def read_file() -> str:
    try:
        with BLACK_LOG.open("r") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def read_file_lines() -> list[str]:
    lines = read_file().splitlines()
    return [line for line in lines if line]


def is_error_line(line: str) -> bool:
    return line.split()[0] == "error:" if line else False


def clean_lines(lines: list[str]) -> list[str]:
    return [line for line in lines if is_error_line(line)]


def is_filename(word: str) -> bool:
    return LEETCODE_DIR in word


def get_filename(error: str) -> str:
    words = error.split()
    filenames = [w for w in words if is_filename(w)]
    if len(filenames) != 1:
        raise Exception("Expected exactly one filename")
    return filenames[0]


def get_filenames(errors: list[str]) -> list[str]:
    return [get_filename(e) for e in errors]


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


def interpret_result(result: bool):
    print("files successfully deleted!" if result else "oops there was an issue")


def run() -> None:
    lines = read_file_lines()
    errors = clean_lines(lines)
    filenames = get_filenames(errors)
    cleaned_filenames = clean_filenames(filenames)
    result = delete_files(cleaned_filenames)
    interpret_result(result)


if __name__ == "__main__":
    run()
