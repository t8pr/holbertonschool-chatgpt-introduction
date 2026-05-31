# ChatGPT Introduction - Debugging & Documentation

This repository focuses on fixing runtime exceptions, handling edge cases, validating user inputs, and adding clear code documentation using AI assistance.

---

## Repository Structure

All completed assignments are located inside the `debugging/` directory:

| File Name | Language | Description / Core Fix |
| :--- | :--- | :--- |
| `factorial.py` | Python | Fixed an infinite loop by decrementing `n`. |
| `print_arguments.py` | Python | Modified indexing to skip printing the script's filename. |
| `change_background.html` | HTML / JS | Fixed a button `id` typo mismatch that broke the event listener. |
| `mines.py` | Python | Added logic to calculate safe cells and trigger a win condition. |
| `factorial_recursive.py` | Python | Structured documentation with *Description*, *Parameters*, and *Returns*. |
| `checkbook.py` | Python | Added `try-except` blocks to prevent crashes on non-numeric inputs. |
| `tic.py` | Python | Fixed turn-swapping bugs, handled draws, and bound input ranges. |

---

## Summary of Tasks

### 0. Python Factorial
* **Problem:** Loop hung forever because the loop counter never changed.
* **Solution:** Added `n -= 1` inside the loop.

### 1. Python Arguments
* **Problem:** Output included the script name (`sys.argv[0]`).
* **Solution:** Sliced the argument range to start tracking from index `1`.

### 2. HTML / JavaScript
* **Problem:** Typo in button ID (`colorButon` vs `colorButton`) returned a `null` object error.
* **Solution:** Aligned the HTML ID with the JavaScript selector spelling.

### 3. Python Mines
* **Problem:** The game never ended even if you cleared all safe squares.
* **Solution:** Implemented a counter to track revealed non-mine blocks for a victory state.

### 4. Python Documentation
* **Problem:** Code lacked explanations.
* **Solution:** Standardized clean recursive function documentation using formal Python docstrings.

### 5. Error Handling
* **Problem:** Entering string letters into a financial float input crashed the runtime engine.
* **Solution:** Implemented a robust `try-except ValueError` verification sequence.

### 6. Tic Tac Toe
* **Problem:** Broken game logic named the wrong winner, ignored ties, and crashed on bad inputs.
* **Solution:** Reorganized loop termination states, added draw verification, and locked grid inputs between coordinates `0` and `2`.

Author Osama Alhamdan
