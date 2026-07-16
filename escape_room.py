# ─────────────────────────────────────────────────────────────
# Escape Room
#
# A text-based Python adventure game where you must escape an
# alien spaceship by solving puzzles, finding a key, and
# navigating through dangerous rooms.
#
# Features:
# - Random door challenge
# - Password puzzle
# - Grid-based movement
# - Key collection
# - Leaderboard saved to a file
#
# Created as a multi-lesson Python project and expanded with
# new features over time.
# ─────────────────────────────────────────────────────────────

import random
import sys
import os

print("Alien Escape")
print("You are trapped on an alien spaceship. Escape before the aliens catch you!")

# Create the leaderboard file if it doesn't exist
if not os.path.exists("leaderboard.txt"):
    open("leaderboard.txt", "w").close()

# Load and display the top scores
with open("leaderboard.txt", "r") as file:
    scores = []

    for line in file:
        name, moves = line.strip().split(", ")
        scores.append((name, int(moves)))

    if scores:
        scores.sort(key=lambda x: x[1])

        print("Top 5 Leaderboard:")
        for name, moves in scores[:5]:
            print(f"{name}: {moves} moves")

# Get the player's name
name = input("What is your name? ")
print(f"Good luck, {name}!")

# Random door challenge
doors = ["1", "2", "3"]
correct_door = random.choice(doors)

door = input("Pick a door (1, 2, or 3): ")

while door != correct_door:
    print("The alien door stays locked.")
    door = input("Pick a door (1, 2, or 3): ")

print("The door opens!")

# Password puzzle
def puzzle():
    words = ["laser", "planet", "galaxy"]
    password = random.choice(words)
    guess_count = 0

    print("An alien computer asks for a password.")

    while guess_count < 3:
        guess = input("Password: ")

        if guess == password:
            print("Correct!")
            return True

        guess_count += 1
        print(f"Wrong! {3 - guess_count} tries left.")

    print("The aliens caught you!")
    sys.exit()

# Game map
# x = wall
# p = puzzle
# k = key
# e = escape pod
# . = empty space
room = [
    "xxxxxx",
    "xp..xx",
    "x.xk.x",
    "x....x",
    "xxxxex",
]

# Tell the player which directions are blocked
def announce_walls(row, col):
    if room[row - 1][col] == "x":
        print("Wall to the north.")
    if room[row + 1][col] == "x":
        print("Wall to the south.")
    if room[row][col - 1] == "x":
        print("Wall to the west.")
    if room[row][col + 1] == "x":
        print("Wall to the east.")

player_row, player_col = 1, 1

# Handle player movement and events
def move(row, col, direction):
    global has_key

    new_row, new_col = row, col

    if direction == "up":
        new_row -= 1
    elif direction == "down":
        new_row += 1
    elif direction == "left":
        new_col -= 1
    elif direction == "right":
        new_col += 1

    # Prevent walking through walls
    if room[new_row][new_col] == "x":
        print("A metal wall blocks your path.")
        return row, col

    # Trigger the puzzle room
    if room[new_row][new_col] == "p":
        puzzle()

    # Pick up the key
    if room[new_row][new_col] == "k":
        has_key = True
        print("You picked up a key.")

    return new_row, new_col

moves = 0
has_key = False

# Main game loop
while True:
    announce_walls(player_row, player_col)
    direction = input("Move (up/down/left/right): ").lower()
    player_row, player_col = move(player_row, player_col, direction)
    moves += 1

    print(f"You are at ({player_row}, {player_col})")

    # Check if the player reached the exit
    if room[player_row][player_col] == "e":
        if has_key:
            break
        else:
            print("You need a key first.")

print("You found the escape pod and escaped the alien spaceship!")
print("You Win!")

# Save the player's score
if os.path.exists("leaderboard.txt"):
    with open("leaderboard.txt", "a") as file:
        file.write(f"{name}, {moves}\n")
