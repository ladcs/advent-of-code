from wrap_around import wrap_around_index

def is_valid_password_puzzle_1(start):
    with open("day1/code.txt", "r") as file:
        password = [0 + int(line[1:]) if line[0] == "R" else 0 - int(line[1:]) for line in file.read().strip().split("\n")]
    
    i = 0

    for step in password:
        start = wrap_around_index(start, step, 100)
        if start == 0: # count 0
            i += 1
    return i



def is_valid_password_puzzle_2(start):
    with open("day1/code.txt", "r") as file:
        password = [0 + int(line[1:]) if line[0] == "R" else 0 - int(line[1:]) for line in file.read().strip().split("\n")]
    i = 0
    for step in password:
        new_start = wrap_around_index(start, step, 100)
        if new_start == 0: # count 0
            i += 1
        complete_cycles = abs(step) // 100
        i += complete_cycles # count all complete cycles
        if start != 0 and new_start != 0: # check partial cycle only if not starting or ending at 0 to not double count 0
            if step > 0:
                if new_start < start:
                    i += 1
            elif step < 0:
                if new_start > start:
                    i += 1
        print(i, start, step, new_start)
        start = new_start
    return i

if __name__ == "__main__":
    is_valid_password_puzzle_2(50)

    """
    erro 1: caso 0 -5 conta
    erro 2: caso 55 -55 nao conta

    --V The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    --V -- The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    --V The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    --V The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    --V The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    --V The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
    """