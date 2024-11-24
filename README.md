# Othello Game

Othello is a classic strategy board game implemented using Python and Pygame. This project recreates the traditional game experience with engaging graphics and smooth gameplay mechanics.

## Features

- **Player vs Computer Mode**: Play against ai using alpha-beta pruning algorithm
- **Player vs Player Mode**: Play against a friend on the same machine.
- **Valid Move Highlighting**: Shows the possible moves for the current player.
- **Score Tracking**: Displays real-time scores for both players.

## Technologies Used

- **Python**: Core programming language.
- **Pygame**: Game development library for rendering graphics and managing game states.

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/AhmedShaaban11/othello.git
    ```
2. **Go to the game directory**
    ```bash
    cd othello
    ```
3. **Install Dependencies:**
    - Ensure Python 3.x is installed.
    - Install Pygame using:
        ```bash
        pip install pygame
        ```

4. **Run the Game:**
    ```bash
    python othello.py
    ```

## How to Play

- Players take turns placing their pieces on the board.
- A valid move must capture at least one opponent piece.
- The game ends when neither player can make a valid move.
- The winner is the player with the most pieces on the board at the end.