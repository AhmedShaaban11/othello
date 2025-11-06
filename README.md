# Othello Game

Othello is a classic strategy board game implemented using Python and Pygame. This project recreates the traditional game experience with engaging graphics and smooth gameplay mechanics.

WATCH THE OVERVIEW [VIDEO](https://drive.google.com/file/d/1ffBjGhZmyssRJrhKJlwWWwscRMxoOps9/view?usp=drive_link)

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

3. **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows with bash
    # or
    venv\Scripts\activate.bat     # On Windows with cmd
    ```

4. **Install Dependencies:**

    - Ensure Python 3.x is installed.
    - Install dependencies using the requirements file:

        ```bash
        pip install -r requirements.txt
        ```

    - **If you encounter path issues**, use the full Python path:

        ```bash
        venv/Scripts/python.exe -m pip install -r requirements.txt
        ```

5. **Run the Game:**

    ```bash
    python main.py
    ```

    - **If you encounter "Unable to create process" errors**, use the full Python path:

        ```bash
        venv/Scripts/python.exe main.py
        ```

## How to Play

- Players take turns placing their pieces on the board.
- A valid move must capture at least one opponent piece.
- The game ends when neither player can make a valid move.
- The winner is the player with the most pieces on the board at the end.

## Troubleshooting

### Issue: "Unable to create process" or Python not found error

- Make sure you have activated your virtual environment first
- If using a virtual environment, you can also run the game directly with:

  ```bash
  venv/Scripts/python.exe main.py  # On Windows
  ```

### Issue: ModuleNotFoundError for pygame

- Ensure you have installed the dependencies:

  ```bash
  pip install -r requirements.txt
  ```

- If the above fails, try using the full Python path:

  ```bash
  venv/Scripts/python.exe -m pip install -r requirements.txt
  ```

### Issue: Virtual Environment Path Mismatch

If you encounter errors like "Fatal error in launcher: Unable to create process", this usually means your virtual environment has path issues:

1. **Deactivate and recreate the virtual environment:**

   ```bash
   deactivate
   rm -rf venv  # Remove the old virtual environment
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
   ```

2. **Alternative: Use absolute paths without activating:**

   ```bash
   # Install dependencies
   ./venv/Scripts/python.exe -m pip install -r requirements.txt
   
   # Run the game
   ./venv/Scripts/python.exe main.py
   ```

### Issue: Permission Errors on Windows

If you encounter permission errors, try running your terminal as administrator or use:

```bash
python -m pip install --user -r requirements.txt
```
