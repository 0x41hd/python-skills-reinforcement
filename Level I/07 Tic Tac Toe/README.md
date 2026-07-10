# Tic-Tac-Toe (Python)

A simple terminal-based Tic-Tac-Toe game for two players: **X** and **O**.

## Game Rules

- Players take turns placing **X** or **O** on a 3x3 grid.
- First player to get **3 in a row** wins (rows, columns, or diagonals).
- If the board is full and nobody wins, the game ends in a **draw**.

## Board Layout

You enter a cell number from **1 to 9**:

```
1 | 2 | 3
----------
4 | 5 | 6
----------
7 | 8 | 9
```

## How to Run

1. Make sure you have **Python 3** installed.
2. From the repo root, run:

```bash
python src/tic\_tac\_toe.py
```

## How to Play

- When prompted: - Enter S to play - Enter Q to quit
  -On each turn: - Enter a cell number (1–9) - The move is accepted only if the cell is empty and the number is valid
- The game ends when:
  - a player wins, or
  - the board is full (draw)

## Features

- Randomly chooses the starting player (X or O)
- Win detection for all 8 winning combinations
- Draw detection when the board is full
- Basic input validation (empty spot + valid range)

## Project Structure

- src/tic_tac_toe.py — Game implementation
- README.md — Project documentation
