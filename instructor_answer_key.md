Instructor Answer Key — Exception Handling Lab
=============================================

Overview
--------
This document provides model solutions, explanations, common student mistakes, and detailed grading notes for each exercise in the `lab_exception_handling` lab.

Exercise 1 — `safe_divide(a, b)`
--------------------------------
Expected behavior
- Return the numeric result of `a / b`.
- If a division by zero occurs, return `None` and do not let an exception propagate.

Model solution
```py
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

Explanation
- Use a `try` block for the division and catch `ZeroDivisionError` specifically.
- Returning `None` communicates the error to the caller without crashing.

Common mistakes
- Catching `Exception` or using a bare `except:` (too broad).
- Returning `0` or another sentinel value that could be mistaken for a real result.
- Not converting to float when needed — note `a / b` in Python 3 already produces float.

Grading notes (30% of lab)
- 20 pts: Correct behavior (returns correct numeric result and `None` on divide-by-zero).
- 5 pts: Use of a specific exception (`ZeroDivisionError`) instead of a bare except.
- 5 pts: Code clarity and small function with docstring.

Exercise 2 — `read_ints(filename)`
---------------------------------
Expected behavior
- Open `filename` and return a list of integers found on non-empty lines.
- If the file does not exist, return an empty list.
- Skip lines that cannot be parsed as integers (do not abort on first parse error).

Model solution
```py
def read_ints(filename):
    ints = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ints.append(int(line))
                except ValueError:
                    continue
    except FileNotFoundError:
        return []
    return ints
```

Explanation
- Wrap the file open in a `try/except FileNotFoundError` to return `[]` when missing.
- For each non-empty line, attempt `int(line)` inside its own `try/except ValueError` so a single bad line is skipped.

Common mistakes
- Letting a `ValueError` from a bad line stop processing the rest of the file.
- Returning strings instead of integers, or returning `None` for a missing file.
- Using a bare `except` that hides unrelated bugs.

Grading notes (30% of lab)
- 20 pts: Correct functional behavior (file missing -> [], skip invalid lines, return ints).
- 5 pts: Robustness (strip lines, skip blanks).
- 5 pts: Readability and small helpers (docstring/tests).

Exercise 3 — `sqrt_positive(n)` and `NegativeNumberError`
------------------------------------------------------
Expected behavior
- Define a custom exception class `NegativeNumberError(Exception)`.
- Convert input to a numeric type (float), return `math.sqrt(n)` for `n >= 0`.
- If `n < 0`, raise `NegativeNumberError` with a clear message.

Model solution
```py
import math

class NegativeNumberError(Exception):
    pass

def sqrt_positive(n):
    val = float(n)
    if val < 0:
        raise NegativeNumberError(f"Negative value: {val}")
    return math.sqrt(val)
```

Explanation
- Converting input to `float` makes the function accept integer and numeric-string inputs consistently.
- Raising a named custom exception makes it easy for callers/tests to detect this specific error case.

Common mistakes
- Using `ValueError` instead of a custom exception (acceptable, but deduct minor points if the spec asked explicitly for a custom class).
- Swallowing exceptions and returning special values instead of raising for invalid negatives.

Grading notes (30% of lab)
- 20 pts: Correct behavior (raises `NegativeNumberError` for negative, computes sqrt otherwise).
- 5 pts: Clear exception message.
- 5 pts: Input normalization (casting to float) and docstring.

Testing & verification (10% of lab)
----------------------------------
- All provided tests should pass. Instructor checks:
  - `safe_divide(6, 3) == 2`, `safe_divide(1, 0) is None`.
  - `read_ints` returns `[1,2,3]` for a file containing `1\n2\nxyz\n3\n` and `[]` for a missing file.
  - `sqrt_positive(4)` returns `2.0` and `sqrt_positive(-1)` raises `NegativeNumberError`.

Suggested feedback snippets for students
- "Good: your function uses a specific exception and returns `None` for divide-by-zero." 
- "Improve: avoid broad `except:` blocks — catch the specific exception you expect." 
- "Nice: your `read_ints` correctly skips malformed lines; consider adding logging for skipped lines." 
- "Note: when asked for a custom exception, define a dedicated exception class rather than reusing `ValueError`." 

Academic integrity & partial credit guidance
- If a student meets functional tests but uses a broad `except`, deduct 2–5 points depending on severity and explain why it's risky.
- If a student returns sentinel values other than `None` (e.g., `0`) for errors, deduct points and offer guidance.

File locations
- Starters: `starters/ex1.py`, `starters/ex2.py`, `starters/ex3.py`
- Solutions: `solutions/sol1.py`, `solutions/sol2.py`, `solutions/sol3.py`
- Tests: `tests/test_exercises.py`

End of answer key
