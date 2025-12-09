from math import sqrt
from typing import Set, Tuple, List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.node = {n: {n} for n in range(n)}

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a:int, b:int)-> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        if rb in self.node.keys():
            self.node[ra].update(self.node[rb])
            del self.node[rb]
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        # print(self.node)
        return True



def distance(point_1: Tuple[str, str, str], point_2: Tuple[str, str, str]) -> float:
    try:
        x1, y1, z1 = point_1
    except:
        print(point_1)
    x2, y2, z2 = point_2
    x0 = int(x1) - int(x2)
    y0 = int(y1) - int(y2)
    z0 = int(z1) - int(z2)
    return sqrt(x0**2 + y0**2 + z0**2)

def read_input(test: bool) -> list[str]:
    pathfile = 'day8/input_test.txt' if test else 'day8/input.txt'
    with open(pathfile, 'r') as f:
        input_points = [tuple(line.strip().split(",")) for line in f.read().split()]
    return input_points

def select_n_lower_distance(points: List[Tuple[float, int, int]], n:int = 10) -> List[Tuple[int, int]]:
    point = sorted(points, key=lambda x: x[0])
    vp = [(p[1],p[2]) for p in point[:n]]
    return vp

def connect_point(list_points: List[Tuple[int, int]]):
    circ = []
    while len(list_points) != 0:
        controler = set(a for a in list_points[0])
        result = [(1, 1)]
        while len(result) != 0:
            result = [t for t in list_points if any(p in t for p in controler)]
            list_points = [x for x in list_points if x not in result]
            controler.update(a for t in result for a in t)
        circ.append(controler)
    return circ
   
def element_by_circ(circts: Set[int]):
    return [len(c) for c in circts]

def sorted_elements(elements: List[int])-> List[int]:
    return sorted(elements, reverse=True)

def find_all_dintance_by_point(points: List[Tuple[int, int, int]]):
    list_tuple_distance_points = []
    for actual_point_index in range(len(points)):
        for next_point_index in range(actual_point_index + 1, len(points)):
            if next_point_index == len(points):
                continue
            list_tuple_distance_points.append((distance(points[actual_point_index], points[next_point_index]), actual_point_index, next_point_index))
    return list_tuple_distance_points

if __name__=="__main__":
    input_list = read_input(False)
    """"
    # parte 1
    list_distance = find_all_dintance_by_point(input_list)
    selected = select_n_lower_distance(list_distance, 11)
    print(selected)
    circts = connect_point(selected)
    print(len(circts))
    # print(circts)
    elements = element_by_circ(circts)
    sorted_elem = sorted_elements(elements)
    mult = 1
    for e in sorted_elem[:3]:
        mult *= e
    print(mult)
    """


    """"
    # parte 1 union find
    k= 10
    n = len(input_list)
    uf = UnionFind(n)
    list_distance = find_all_dintance_by_point(input_list)
    selected = select_n_lower_distance(list_distance, n)

    added = 0
    idx = 0
    while added < k and idx < len(selected):
        print(selected[idx])
        a, b = selected[idx]
        if uf.union(a, b):
            added += 1
        idx += 1
    
    comp_sizes = {}
    for i in range(n):
        root = uf.find(i)
        comp_sizes[root] = uf.size[root]
        print(comp_sizes)

    top3 = sorted(comp_sizes.values(), reverse=True)[:3]
    result = top3[0] * top3[1] * top3[2]
    """

    # parte 1 com union find
    """"
    k = 20
    n = len(input_list)
    uf = UnionFind(n)
    list_distance = find_all_dintance_by_point(input_list)
    selected = select_n_lower_distance(list_distance, n)

    added = 0
    for i in range(k):
        a, b = selected[i]
        uf.union(a, b)
    
    
    comp_sizes = {}
    for i in range(n):
        root = uf.find(i)
        comp_sizes[root] = uf.size[root]

    top3 = sorted(comp_sizes.values(), reverse=True)[:3]
    result = top3[0] * top3[1] * top3[2]
    print(result)
    """


    n = len(input_list)
    uf = UnionFind(n)
    map_input = {i: input_list[i] for i in range(len(input_list))}
    list_distance = find_all_dintance_by_point(input_list)
    selected = select_n_lower_distance(list_distance, len(list_distance))

    added = 0
    i = 0
    last_step = ()
    while len(uf.node) > 1 and i < len(selected):
        a, b = selected[i]
        if uf.union(a, b):
            last_step = (a, b)
        i += 1

    p1, p2 = last_step[0], last_step[1]
    xa, _, _ = map_input[p1]
    xb, _, _ = map_input[p2]

    print(int(xa)*int(xb))