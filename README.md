# Mastermind Game - Python Implementation

## Overview
This project is an individual coursework assignment for the module **DOC 313 Introduction to Programming in Python** at the Informatics Institute of Technology. The assignment, submitted by **Nemsara Ranaba** (Student ID: 20221241), implements a Mastermind-style deduction game where players guess a hidden sequence of colors represented by numbers.

## Project Details
- **Module**: DOC 313 Introduction to Programming in Python - P1
- **Module Leader**: Mr. Sudharshan Welihinda
- **Assignment Number**: 1
- **Assignment Type**: Individual Coursework
- **Submission Date**: 12th December 2022
- **Deadline**: On or before 9:00 AM
- **Student Name**: Nemsara Ranaba
- **Student ID**: 20221241

## Game Description
The Mastermind game involves:
- A code maker who secretly selects four colored pegs (represented by numbers 1–6, mapped to colors: White, Blue, Red, Yellow, Green, Purple).
- A code breaker who attempts to guess the sequence within 8 attempts.
- The player inputs four numbers (0–6), and the system provides feedback:
  - "1" for a correct number in the correct position.
  - "0" for a correct number in the wrong position.
  - "." for an incorrect number.
- Entering "0000" terminates the game.
- Invalid inputs (numbers outside 0–6) prompt an error message.
- After each game, the player can choose to continue or exit.

## File Structure
- **Report.pdf**: The main report document containing:
  - Introduction to the problem.
  - Pseudocode explaining the program logic.
  - Python code for the game (though incomplete in the provided document).
  - Screenshots of the working program (positive and negative cases).
  - Conclusion summarizing the game logic.
- **README.md**: This file, providing an overview of the project.

## Program Features
- **Player Input**: Prompts the user to enter their name and displays a welcome message.
- **Random Code Generation**: Generates four random numbers (1–6) using Python’s `random` module.
- **Color Mapping**: Maps numbers to colors (1: White, 2: Blue, 3: Red, 4: Yellow, 5: Green, 6: Purple).
- **Input Validation**: Ensures guesses are within 0–6; displays "Invalid number" for invalid inputs.
- **Game Loop**: Allows up to 8 attempts per game, with the option to continue or exit after each round.
- **Feedback System**: Provides feedback on guesses using "1", "0", or "." based on correctness and position.
- **Termination**: Exits the game if "0000" is entered or after 8 attempts if the player chooses not to continue.

## How to Run
1. Ensure Python 3.x is installed.
2. Copy the Python code from the report (Section 3, though incomplete in the provided document) into a `.py` file.
3. Run the script in a Python environment.
4. Follow the prompts to:
   - Enter your name.
   - Input four numbers (0–6) per guess.
   - Enter "0000" to terminate the game.
   - Choose "yes" or "no" to continue after winning or completing 8 attempts.

## Notes
- The provided report lacks the complete Python code in Section 3 (pages 12–13). Users must refer to the pseudocode (pages 5–10) to reconstruct the full implementation.
- Screenshots (pages 14–17) demonstrate positive and negative test cases, but the content appears incomplete or corrupted (repetitive "111" entries).
- The game logic is based on the classic Mastermind board game, adapted for a command-line interface.

## Limitations
- The report’s Python code section is incomplete, requiring users to implement the full code based on pseudocode.
- The feedback mechanism in the pseudocode has redundant and inconsistent conditions (e.g., repeated `result4 = "0"` in page 9), which may need correction.
- No scoring system is detailed beyond a placeholder "XXX points" in the pseudocode.

## Conclusion
This project demonstrates fundamental Python programming concepts, including random number generation, conditional statements, loops, and user input handling. The game successfully implements the core mechanics of Mastermind, with clear feedback for user guesses and robust input validation.

For further details, refer to the **Report.pdf** included in the project submission.