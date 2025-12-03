def count_zero_crossings(start, step, size=100):
    if step == 0:
        return 0
    
    direction = 1 if step > 0 else -1
    total_steps = abs(step)

    # Número de vezes que passa pelo zero = quantas vezes o ponteiro dá voltas completas
    full_cycles = total_steps // size

    # Agora conta a parte parcial que sobra
    leftover = total_steps % size

    crosses = full_cycles

    # posição atual, depois o próximo passo
    pos = start
    end_pos = (start + step) % size

    # verificar se nesse "leftover" cruzou o zero
    if direction == 1:  # girando para a direita
        if (pos < size - leftover and end_pos < pos) or leftover > (size - pos - 1):
            crosses += 1
    else:  # girando para a esquerda
        if (pos >= leftover and end_pos > pos) or leftover > pos:
            crosses += 1

    return crosses

def solve(start):
    count = 0

    with open("day1/code.txt") as f:
        steps = [int(line[1:]) if line[0] == "R" else -int(line[1:])
                 for line in f.read().strip().splitlines()]

    for step in steps:
        count += count_zero_crossings(start, step)
        start = (start + step) % 100

    return count

if __name__ == "__main__":
    print("Puzzle 2:", solve(50))