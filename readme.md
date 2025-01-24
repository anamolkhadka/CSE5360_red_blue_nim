# Red-Blue Nim Game (Min-Max Problem)

## Overview

This project is an implementation of the **Red-Blue Nim** game using the **Min-Max algorithm with Alpha-Beta Pruning**, designed as part of an AI coursework assignment. The game features two versions: **standard** and **misère**, with the goal of optimizing the computer's strategy to either win or minimize losses based on the rules of the version being played.

---

## Min-Max Game Description

The **Min-Max algorithm** is a decision-making strategy used in two-player games such as chess, tic-tac-toe, and nim. The objective of the algorithm is to minimize the possible loss in the worst-case scenario while maximizing the potential gain.

### Key Features of the Min-Max Algorithm
- A game tree is constructed to evaluate all possible future moves.
- Each node in the tree represents a possible game state.
- The algorithm alternates between minimizing the opponent's advantage and maximizing the player's advantage.
- **Alpha-Beta Pruning** optimizes the search by eliminating unnecessary branches, improving computational efficiency.

---

## Red-Blue Nim Game Rules

### The game consists of two piles of marbles:
- **Red marbles** (worth 2 points each)
- **Blue marbles** (worth 3 points each)

### Gameplay:
- Players take turns removing **1 or 2 marbles** from a single pile.
- If a player is left with an empty pile on their turn:
  - **Standard version:** They lose.
  - **Misère version:** They win.
- The game ends when either pile is empty.

### Scoring:
- In the **standard version**, the losing player is penalized based on the number of marbles left.
- In the **misère version**, the winning player gains points based on the remaining marbles.

---

## Project Structure

The project consists of the following files:

- **`red_blue_nim.py`** – Main program file containing the game logic and Min-Max implementation.
- **`README.md`** – Instructions and details about the project.
- **`evalfunction.txt`** – Explanation of the evaluation function used for depth-limited search.
- **`training_data.txt`** – Example test cases and game scenarios.

---

## How It Works

### Input Format

The program is executed with the following command:

```bash
python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>