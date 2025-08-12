"""Simple terminal-based Snake game using curses.

The player controls the snake with the arrow keys and attempts to eat
food without colliding with the snake's body or the window borders.
"""

import curses
import random
from typing import List, Tuple


Position = Tuple[int, int]


def create_food(snake: List[Position], height: int, width: int) -> Position:
    """Generate coordinates for food not overlapping the snake."""
    while True:
        pos = (random.randint(1, height - 2), random.randint(1, width - 2))
        if pos not in snake:
            return pos


def main(stdscr: "curses._CursesWindow") -> None:
    """Run the main game loop."""
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(True)
    stdscr.timeout(100)  # 100 ms per frame

    height, width = stdscr.getmaxyx()
    win = curses.newwin(height, width, 0, 0)
    win.keypad(True)
    win.border(0)

    # Initial snake: three segments in the middle of the screen
    snake: List[Position] = [
        (height // 2, width // 2 + i) for i in range(3)
    ]
    direction = curses.KEY_LEFT

    food = create_food(snake, height, width)
    score = 0

    while True:
        next_key = win.getch()
        if next_key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT):
            direction = next_key

        head_y, head_x = snake[0]
        if direction == curses.KEY_UP:
            head_y -= 1
        elif direction == curses.KEY_DOWN:
            head_y += 1
        elif direction == curses.KEY_LEFT:
            head_x -= 1
        elif direction == curses.KEY_RIGHT:
            head_x += 1
        new_head = (head_y, head_x)

        # Check collisions
        if (
            head_y in (0, height - 1)
            or head_x in (0, width - 1)
            or new_head in snake
        ):
            msg = f"Game over! Score: {score}"
            win.addstr(height // 2, (width - len(msg)) // 2, msg)
            win.refresh()
            curses.napms(2000)
            break

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = create_food(snake, height, width)
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], " ")

        win.addch(food[0], food[1], "*")
        win.addch(new_head[0], new_head[1], "#")


if __name__ == "__main__":
    curses.wrapper(main)
