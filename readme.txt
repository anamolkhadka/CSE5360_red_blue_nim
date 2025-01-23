Name: Anamol Khadka
UTA ID: 1001747990
Email: anamol.khadka@mavs.uta.edu

Programming language - Python/Python3
Version - 3.12.4

Hello, please rest all the instructions below before testing the program.


Code Structured

Game Initialization

1. Define marble weights (red_score, blue_score).
    - Set move ordering based on game version (standard_moves and misere_moves).
    - Parse command-line arguments for game configuration (number of marbles, version, first player, depth limit).

2. Core Functions

    - minimax(): Implements depth-limited Minimax with Alpha-Beta pruning.
    - calculate_score(): Calculates utility score for terminal nodes.
    - evaluate(): Heuristic evaluation function for non-terminal nodes when depth limit is reached.
    - get_best_move(): Determines the optimal move for the computer using Minimax.

3. Game Loop

    - Alternates between the computer and human turns.
    - Computer Turn: Calls get_best_move() to make a move.
    - Human Turn: Prompts user input for move selection.

4. End-of-Game Calculation

    - Uses calculate_score() to determine the winner based on the final marble configuration.

5. Command-Line Interface (CLI)

    - Parses and validates input, displaying usage instructions for invalid commands.


How to run the code ?

Without the depth limited MinMax search.(Regular version)
- python3 red_blue_nim.py 2 1 standard computer (standard)
- python3 red_blue_nim.py 2 1 misere computer (misere)

With the depth limited MinMax search (Extra Credit version)
- See evalfunction.txt for details about the evalfunction used for the depth limited MinMax search with alpha beta pruning.

First run the program with higher number of balls without depth limit.
- python3 red_blue_nim.py 5 4 standard computer
- python3 red_blue_nim.py 5 4 standard computer 2

Note: When using the depth limit please provide the version name and first player since the depth limit is argv[5].


See screenshots for the demo in the screenshots directory !

Let me know, if there is any issues. The program should run perfectly for both the normal version
and the extra credit version as expected.

Thank you,
Anamol Khadka