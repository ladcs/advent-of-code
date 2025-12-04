def start_value(start, end, length):
    new_start = "1" + "0" * (length + 1)
    new_start = int(start)
    end = int(end)
    if new_start > end or new_start < int(start):
        return None
    return str(new_start)

def check_pair_of_digits(length_start, length_end, start, end, invalid_id):
    if length_start % 2 != 0 and length_end == length_start:
        return []
    elif length_start % 2 != 0 and length_end % 2 == 0:
        start = start_value(start, end, length_start)
    if start is None:
        return []
    end = int(end)
    start_check_number = start[:length_start // 2] if length_start // 2 > 0 else "1"
    invalid_id = []
    for i in range(int(start_check_number), end):
        check_id = int(str(i) * 2)
        if check_id >= int(start) and check_id <= end:
            invalid_id.append(check_id)
        if check_id >= end:
            break
    return invalid_id


def invalid_id_puzzle_1(test: bool = False):
    pathfile = "day2/ids_test.txt" if test else "day2/ids.txt"
    with open(pathfile, "r") as file:
        codes = [line.strip() for line in file.read().strip().split(",")]

    invalid_id = []
    for code in codes:
        start, end = code.split("-")
        length_start = int(len(start))
        length_end = int(len(end))
        invalid_id.extend(check_pair_of_digits(length_start, length_end, start, end, invalid_id))
    return sum(invalid_id)

def is_invalid(num: int) -> bool:
    s = str(num)
    n = len(s)
    
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            chunk = s[:k]
            if chunk * (n // k) == s:
                return True
    return False


def invalid_id_puzzle_2(test: bool = True):
    pathfile = "day2/ids_test.txt" if test else "day2/ids.txt"
    invalid_ids = []

    with open(pathfile) as f:
        codes = [line.strip() for line in f.read().strip().split(",")]

    for code in codes:
        start, end = map(int, code.split("-"))

        for num in range(start, end + 1):
            if is_invalid(num):
                invalid_ids.append(num)

    return sum(invalid_ids)

if __name__ == "__main__":
    print(invalid_id_puzzle_2())

