'''
- Red marble weight: 2
- Blue marble weight: 3
- For computer standard move - 2R, 2B, 1R, 1B
- For computer misere move - 1B, 1R, 2B, 2R
- If it is your turn and if either pile is empty (only one color left) then you lose in the standard version of the game and win in the misere version.
'''

import sys

def red_blue_nim(num_red, num_blue, version='standard', first_player='computer', depth=None):
    # Scoring weights for marbles
    red_score = 2
    blue_score = 3

    # Move ordering based on the game version
    standard_moves = [(2, 'red'), (2, 'blue'), (1, 'red'), (1, 'blue')]
    misere_moves = [(1, 'blue'), (1, 'red'), (2, 'blue'), (2, 'red')]
    # Set move ordering to default to standard moves if nothing is mentioned
    move_order = standard_moves if version == 'standard' else misere_moves

    # Minimax function with Alpha-Beta Pruning
    def minimax(red, blue, is_maximizing, alpha, beta, current_depth, max_depth):
        if red == 0 or blue == 0:  # Terminal state
            if version == 'standard':
                return -calculate_score(red, blue) if is_maximizing else calculate_score(red, blue)
            else:
                return calculate_score(red, blue) if is_maximizing else -calculate_score(red, blue)
        
        if max_depth is not None and current_depth >= max_depth:
            return evaluate(red, blue)

        if is_maximizing:
            max_eval = float('-inf')
            for move in move_order:
                marbles, color = move
                if color == 'red' and red >= marbles:
                    new_red, new_blue = red - marbles, blue
                elif color == 'blue' and blue >= marbles:
                    new_red, new_blue = red, blue - marbles
                else:
                    continue
                evaluation = minimax(new_red, new_blue, False, alpha, beta, current_depth + 1, max_depth)
                max_eval = max(max_eval, evaluation)
                alpha = max(alpha, evaluation)
                #Pruning occurs here.
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in move_order:
                marbles, color = move
                if color == 'red' and red >= marbles:
                    new_red, new_blue = red - marbles, blue
                elif color == 'blue' and blue >= marbles:
                    new_red, new_blue = red, blue - marbles
                else:
                    continue
                evaluation = minimax(new_red, new_blue, True, alpha, beta, current_depth + 1, max_depth)
                min_eval = min(min_eval, evaluation)
                beta = min(beta, evaluation)
                #Pruning occurs here.
                if beta <= alpha:
                    break
            return min_eval

    # Function to calculate the score
    def calculate_score(red, blue):
        return (red * red_score) + (blue * blue_score)

    # Evaluate function for non-terminal nodes
    def evaluate(red, blue):
        return (red * red_score) + (blue * blue_score)

    # Function to get the best move for the computer
    def get_best_move(red, blue):
        best_score = float('-inf')
        best_move = None
        for move in move_order:
            marbles, color = move
            if color == 'red' and red >= marbles:
                new_red, new_blue = red - marbles, blue
            elif color == 'blue' and blue >= marbles:
                new_red, new_blue = red, blue - marbles
            else:
                continue
            score = minimax(new_red, new_blue, False, float('-inf'), float('inf'), 0, depth)
            if score > best_score:
                best_score = score
                best_move = (marbles, color)
        return best_move

    # Game loop
    current_player = first_player
    while num_red > 0 and num_blue > 0:
        if current_player == 'computer':
            move = get_best_move(num_red, num_blue)
            if move:
                marbles, color = move
                print(f"\nComputer removes {marbles} {color} marble(s).")
                if color == 'red':
                    num_red -= marbles
                else:
                    num_blue -= marbles
                # Show current game state
                print(f"Current game state: {num_red} red marbles, {num_blue} blue marbles remaining.")
            current_player = 'human'
        else:
            while True:
                try:
                    marbles = int(input("\nEnter number of marbles to remove (1 or 2): "))
                    color = input("Enter color (red or blue): ").strip().lower()
                    if marbles not in [1, 2] or color not in ['red', 'blue']:
                        raise ValueError("Invalid input. Please enter 1 or 2 for marbles and 'red' or 'blue' for color.")
                    if (color == 'red' and num_red >= marbles) or (color == 'blue' and num_blue >= marbles):
                        if color == 'red':
                            num_red -= marbles
                        else:
                            num_blue -= marbles
                        # Show current game state after human move
                        print(f"Current game state: {num_red} red marbles, {num_blue} blue marbles remaining.")
                        current_player = 'computer'
                        break
                    else:
                        print("Invalid move. Not enough marbles in the selected pile. Try again.")
                except ValueError as e:
                    print(e)

    # Determine the result
    final_score = calculate_score(num_red, num_blue)
    if (version == 'standard' and current_player == 'computer') or (version == 'misere' and current_player == 'human'):
        print(f"\nComputer loses. Human wins. Final score: {final_score}")
    else:
        print(f"\nComputer wins. Human loses. Final score: {final_score}")

# Command-line interface
if __name__ == "__main__":
    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    version = sys.argv[3] if len(sys.argv) > 3 else 'standard'
    first_player = sys.argv[4] if len(sys.argv) > 4 else 'computer'
    depth = int(sys.argv[5]) if len(sys.argv) > 5 else None
    red_blue_nim(num_red, num_blue, version, first_player, depth)