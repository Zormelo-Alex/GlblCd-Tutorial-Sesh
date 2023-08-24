def print_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(grid, player):
    for row in grid:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(grid[row][col] == player for row in range(3)):
            return True

    if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(grid):
    return all(cell != " " for row in grid for cell in row)

def main():
    grid = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_grid(grid)
        x, y = map(int, input(f"Player {players[current_player]}, enter coordinates (x, y): ").split(','))

        if grid[x][y] == " ":
            grid[x][y] = players[current_player]

            if check_winner(grid, players[current_player]):
                print_grid(grid)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_draw(grid):
                print_grid(grid)
                print("It's a draw!")
                break

            current_player = (current_player + 1) % 2
        else:
            print("That cell is already occupied. Try again.")

if __name__ == "__main__":
    main()
