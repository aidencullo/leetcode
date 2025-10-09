# Gemini Code Assistant Context

## Project Overview

This repository contains solutions to LeetCode problems, implemented in Python. Each problem has its own dedicated directory, named after the problem number.

## Directory Structure

The repository is organized as follows:

- **`/<problem_number>/`**: A directory for each LeetCode problem.
  - **`solution.py`**: Contains one or more Python solutions for the problem.
  - **`test_solution.py`**: Contains `pytest` tests to verify the correctness of the solution(s).

## Development Conventions

- **Solutions**: Solutions are implemented as methods within a `Solution` class in the `solution.py` file. Multiple solution approaches may be present in the same file.
- **Testing**: The `pytest` framework is used for testing. Tests are located in the `test_solution.py` file and use `pytest.mark.parametrize` to test multiple input cases.

## Building and Running

There is no central build process. To run the tests for a specific problem, you can use `pytest` from within the problem's directory.

For example, to run the tests for problem 1:

```bash
cd 1
pytest
```
