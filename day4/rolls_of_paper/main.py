from pprint import pprint

def get_border_rolls(matrix):
    rows, cols = len(matrix), len(matrix[0])
    border = set()
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] != "@":
                continue

            if r in (0, rows-1) or c in (0, cols-1):
                border.add((r,c))
                continue

            if any(matrix[r+dr][c+dc] == "." for dr,dc in dirs):
                border.add((r,c))
    return list(border)


def is_accessible_rolls(matrix, border_roll):
    row = border_roll[0]
    column = border_roll[1]
    rows, cols = len(matrix), len(matrix[0])

    if row in (0, rows-1) and column in (0, cols-1):    
        return True
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    roll_adj = 0
    for dr, dc in dirs:
        r, c = row + dr, column + dc
        if 0 <= r < rows and 0 <= c < cols:
            if matrix[r][c] == "@":
                roll_adj += 1
                if roll_adj >= 4:
                    return False
    return True
    

def find_accessible_rolls(matrix):
    border_rolls = get_border_rolls(matrix)
    access = 0
    rolls_can_access = []
    for roll in border_rolls:
        if is_accessible_rolls(matrix, roll):
            rolls_can_access.append(roll)
            access += 1
    # print(access) # part 1
    return rolls_can_access, access

if __name__ == "__main__":
    test = False
    filepath = "day4/papers_test.txt" if test else "day4/papers.txt"
    with open(filepath, "r") as f:
        matrix = [list(line.strip()) for line in f.read().strip().split("\n")]
    removed_rolls = 0
    access = 1
    while access != 0:
        rolls, access = find_accessible_rolls(matrix)
        for roll in rolls:
            matrix[roll[0]][roll[1]] = "."
        removed_rolls += access
    print(removed_rolls)

    

    










"""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

"""
"""
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
"""