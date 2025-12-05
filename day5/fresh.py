def get_inters(inter_list):
    inters = []
    for i in inter_list:
        a, b = i.split("-")
        inters.append((int(a), int(b)))
    return inters

def is_item_between_inters(item, inters):
    for start, end in inters:
        if start <= item <= end:
            return True
    return False

def merge_interval(inters):
    inters = sorted(inters, key= lambda x: x[0])
    cur_start, cur_end = inters[0]

    merged = []

    for start, end in inters:
        if cur_end + 1 >= start:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end
    
    merged.append((cur_start, cur_end))
    return merged


if __name__=="__main__":
    test = False
    with open("day5/ids_test.txt" if test else "day5/ids.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    empty_index = lines.index("")

    inter_list = lines[:empty_index]
    itens_list = lines[empty_index+1:]

    inters = get_inters(inter_list)
    
    inters = merge_interval(inters)

    # fresh_itens = 0
    # for item in itens_list:
    #     if is_item_between_inters(int(item), inters):
    #         fresh_itens += 1
    
    # print(fresh_itens) # part 1

    fresh = sum([inter[1] - inter[0] + 1 for inter in inters])
    print(fresh)