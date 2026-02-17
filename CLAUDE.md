# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a LeetCode solutions repository containing Python solutions organized by problem number. Each problem has its own directory (e.g., `1/`, `482/`, `1736/`).

## Directory Structure

- `/<problem_number>/solution.py` - Python solution(s) implementing a `Solution` class
- `/<problem_number>/test_solution.py` - Optional pytest or unittest tests (most problems don't have test files)
- `/tld/` - Haskell practice files (unrelated to LeetCode)

## Running Tests

Run tests for a specific problem from the problem directory:

```bash
cd <problem_number>
pytest
```

Or run directly:

```bash
pytest <problem_number>/test_solution.py
```

## Code Conventions

- Solutions are methods within a `Solution` class
- Multiple solution approaches may exist in the same file
- Tests use `pytest.mark.parametrize` or `unittest.TestCase`

## Commit Message Format

Use descriptive messages with problem number:
- `feat: Solve problem 482 (License Key Formatting)`
- `fix: Problem 401 edge case handling`

## Current Problems

- 824: Goat Latin (Easy) - stub

## Skills and Agents

- Use `/leetcode` skill to work on LeetCode problems in this directory
- The `leetcode-code-reviewer` agent provides algorithmic feedback and optimization suggestions for solutions
