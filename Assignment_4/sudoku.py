def print_grid(grid):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            
            print(grid[row][col] if grid[row][col] != 0 else ".", end=" ")
        print()


def find_unassigned(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


def is_valid(grid, value, position):
    row, col = position

    # Row constraint
    for c in range(9):
        if grid[row][c] == value and c != col:
            return False

    # Column constraint
    for r in range(9):
        if grid[r][col] == value and r != row:
            return False

    # 3x3 subgrid constraint
    box_row = row // 3
    box_col = col // 3

    for r in range(box_row * 3, box_row * 3 + 3):
        for c in range(box_col * 3, box_col * 3 + 3):
            if grid[r][c] == value and (r, c) != position:
                return False

    return True


def backtrack(grid):
    unassigned = find_unassigned(grid)
    if not unassigned:
        return True

    row, col = unassigned

    for value in range(1, 10):
        if is_valid(grid, value, (row, col)):
            grid[row][col] = value

            if backtrack(grid):
                return True

            grid[row][col] = 0  # backtrack

    return False


# Example Sudoku (0 = empty)
grid = [
    [0,0,3,0,2,0,6,0,0],
    [9,0,0,3,0,5,0,0,1],
    [0,0,1,8,0,6,4,0,0],
    [0,0,8,1,0,2,9,0,0],
    [7,0,0,0,0,0,0,0,8],
    [0,0,6,7,0,8,2,0,0],
    [0,0,2,6,0,9,5,0,0],
    [8,0,0,2,0,3,0,0,9],
    [0,0,5,0,1,0,3,0,0]
]

print("Initial Sudoku:\n")
print_grid(grid)

if backtrack(grid):
    print("\nSolved Sudoku:\n")
    print_grid(grid)
else:
    print("No solution exists")
