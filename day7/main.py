from pprint import pprint
from typing import Tuple

def read_input(test: bool = True):
    with open("day7/input_test.txt" if test else "day7/input.txt", "r") as f:
        matriz = [list(r) for r in f.read().split()]
    
    return matriz

def is_div(matriz: list, point: Tuple[int, int]) -> bool:
    if matriz[point[1]] > 0:
        return True
    return False

def find_sep(matriz: list[list]):
    count = 0
    counter = [0 for _ in matriz[0]]
    for r in range(len(matriz)):
        for c in range(len(matriz[r])):
            if matriz[r][c] == "S":
                counter[c] = 1
            if matriz[r][c] == "^":
                if is_div(counter, (r,c)):
                    count += 1
                    counter[c-1] += counter[c]
                    counter[c+1] += counter[c]
                    counter[c] = 0
    print(sum(counter))
    print(count)
    return count

if __name__ == "__main__":
    matriz = read_input(False)
    find_sep(matriz)
