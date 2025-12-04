from wrap_around import wrap_around_index

def valid_password_puzzle_1(start):
    with open("day1/code.txt", "r") as file:
        password = [0 + int(line[1:]) if line[0] == "R" else 0 - int(line[1:]) for line in file.read().strip().split("\n")]
    
    i = 0

    for step in password:
        start = wrap_around_index(start, step, 100)
        if start == 0: # count 0
            i += 1
    return i



def valid_password_puzzle_2(start):
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
        start = new_start
    return i

if __name__ == "__main__":
    print(valid_password_puzzle_2(50))