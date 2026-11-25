# 🔢 The Secret Digit

A simple command-line number guessing game written in Python.
The computer picks a secret number between **0 and 100**, and you have **3 attempts** to guess it. After every wrong guess you get a hint: too low or too high.

## Features

- Random secret number from 0 to 100
- 3 attempts per round with "too low / too high" hints
- Input validation (non-numbers and out-of-range values don't cost an attempt)
- Play as many rounds as you like
- No external dependencies, only Python's standard library

## Requirements

- Python 3.6 or newer

## Getting Started

```bash
git clone https://github.com/leVoidRaptor/The-Secret-Digit.git
cd The-Secret-Digit
python The-Secret-Digit.py
```

## How to Play

1. Press `S` to start a round or `F` to exit.
2. Enter a whole number between 0 and 100.
3. Read the hint and try again, you have 3 attempts in total.
4. After the round, press `Y` to play again or `N` to quit.

## Example

```text
Welcome to The Secret Digit!
Press S to continue or F to exit: s
The computer has selected a random number. You have 3 attempts to guess it!
First guess: 50
Your guess is too low! Try again.
Second guess: 75
Your guess is too high! Try again.
Third guess: 62
Correct! You guessed the number!
Number: 62	Your guess: 62
Attempts: 3
Do you want to play again? (Y/N): n
Goodbye!
```
