def max_joltage(string_batteries, size_battery=12):
    list_batteries = [int(c) for c in string_batteries]
    joltage_list = list_batteries[:-(size_battery - 1)]
    aux = len(joltage_list)
    highest  = ""
    for i in range(size_battery):
        selected = max(joltage_list)
        index_selected = list_batteries[:aux + 1].index(selected)
        list_batteries = list_batteries[index_selected + 1:]
        aux -= index_selected
        joltage_list = list_batteries[:aux]
        highest += str(selected)
        # joltage_list = list_batteries[list_batteries.index(max(selected)) + len(highest):]
    return int(highest)

def total_output_joltage_1(test=False):
    filepath = "day3/battery_test.txt" if test else "day3/battery.txt"
    with open(filepath, "r") as f:
        batteries = [line.strip() for line in f.read().strip().split("\n")]
    sum_joltage = sum([max_joltage(battery, 2) for battery in batteries])
    return sum_joltage

def total_output_joltage_2(test=False):
    filepath = "day3/battery_test.txt" if test else "day3/battery.txt"
    with open(filepath, "r") as f:
        batteries = [line.strip() for line in f.read().strip().split("\n")]
    sum_joltage = sum(map(max_joltage, batteries))
    return sum_joltage



if __name__ == "__main__":
    print(max_joltage("987654321111111", 12)) # 987654321111
    print(max_joltage("811111111111119", 12)) # 811111111119
    print(max_joltage("234234234234278", 12)) # 434234234278
    print(max_joltage("818181911112111", 12)) # 888911112111

    print(total_output_joltage_1(True))
