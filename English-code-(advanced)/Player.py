import os
import sys

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

class Player:
    def __init__(self, is_first_player: bool):
        self.is_first_player = is_first_player

    def play(self, grid):
        print("Player %s, it's your turn!" % ("1" if self.is_first_player else "2"))

        def get_key():
            key = msvcrt.getch()
            try:
                return key.decode()
            except UnicodeDecodeError:  # A keypress couldn't be decoded
                # is it an arrow key?
                if key == b"\xe0":
                    key = msvcrt.getch()
                    if key == b"H":
                        return "up"
                    if key == b"P":
                        return "down"
                    if key == b"K":
                        return "left"
                    if key == b"M":
                        return "right"
                elif key == b'\r':  # Enter key
                    return "enter"

        cursor_row, cursor_col = 0, 0

        def print_grid():
            os.system('cls' if os.name == 'nt' else 'clear')
            for r, row in enumerate(grid):
                for c, col in enumerate(row):
                    if r == cursor_row and c == cursor_col:
                        print("[P]", end=" ")
                    else:
                        print(f"[{col}]", end=" ")
                print()

        print_grid()
        while True:
            key = get_key()
            # print(key)
            if key == 'a':
                break
            elif key == 'z' or key == 'up' and cursor_row > 0:
                cursor_row -= 1
            elif key == 's' or key == 'down' and cursor_row < len(grid) - 1:
                cursor_row += 1
            elif key == 'q' or key == 'left' and cursor_col > 0:
                cursor_col -= 1
            elif key == 'd' or key == 'right' and cursor_col < len(grid[0]) - 1:
                cursor_col += 1
            elif key == 'enter':
                if self.is_first_player and grid[cursor_row][cursor_col] == ' ':
                    grid[cursor_row][cursor_col] = 'X'
                else:
                    grid[cursor_row][cursor_col] = 'O'

            print_grid()

# Example usage:
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

player1 = Player(True)
player1.play(grid)