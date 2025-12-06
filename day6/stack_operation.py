from pprint import pprint

def sum(a: int, b: int):
    return a + b

def mult(a:int, b:int):
    return a * b

def get_stack_1(test:bool = True):
    path = 'day6/equation_test.txt' if test else 'day6/equation.txt'
    matrix = []
    with open(path, 'r') as f:
        matrix = [" ".join(line.split()).split() for line in f.readlines()]
    return matrix

def get_stack_2(test:bool = True):
    path = 'day6/equation_test.txt' if test else 'day6/equation.txt'
    with open(path, 'r') as f:
        lines = f.read().split("\n")
    
    cols = list(zip(*lines))

    print(cols)

    test = ["".join(c).replace(" ", "") for c in cols]

    print(test)

    all_sum = 0
    aux = 1
    for t in range(len(test)):
        if test[t] == "":
            # print(aux)
            all_sum += aux if simbolo == "*" else aux -1
            aux = 1
            simbolo = ""
            continue
        elif "*" in test[t]:
            simbolo = "*"
            test[t]= test[t].replace("*", "")
        elif "+" in test[t]:
            simbolo = "+"
            test[t]= test[t].replace("+", "")
        aux = sum(aux, int(test[t])) if simbolo == "+" else mult(aux, int(test[t]))
    # print(aux)
    all_sum += aux if simbolo == "*" else aux - 1
    # print(all_sum)
    return
    last_line = lines[len(lines) - 1]
    test = []
    count = 0
    for i in range(len(last_line)):
        if last_line[i] == " ":
            count += 1
        if (last_line[i] == "*" or last_line[i] == "+"):
            test.append(count)
            count = 0
    test.append(count + 1)

    test = test[1:]
    matrix = [[] for i in lines]

    for i in range(len(lines)):
        start = 0
        for j in range(len(test)):
            matrix[i].append(lines[i][start:start + test[j]])
            start += 1 + test[j]
    
    matrix_aux = list(map(list, zip(*matrix)))
    aux_list = []

    pprint(matrix)
    for i in range(len(matrix_aux)):
        aux = ""
        for t in range(test[i]):
            for j in range(len(matrix_aux[i][:-1])):
                aux += matrix_aux[i][j][test[i]-t-1]
            aux_list.append(aux)
            aux = ""
        for j in range(len(aux_list)):
            matrix[j][i] = int(aux_list[j].strip())
        aux_list = []
    

    for i in range(len(matrix[-1])):
        matrix[-1][i] = matrix[-1][i].replace(" ", "")

    return matrix
    
def resolve_operation(matrix):
    result = 0
    to_debug = ""
    for i in range(len(matrix[0])):
        result_operation = 1
        operation = matrix[len(matrix) - 1][i]
        for j in range(len(matrix) - 1):
                number = int(matrix[j][i])
                to_debug += f'{operation}{number}'
                result_operation = sum(result_operation, number) if operation == "+" else mult(result_operation, number)
        if operation == "+":
            result_operation -= 1
        print(f'{to_debug}= {result_operation}')
        result += result_operation
        to_debug = ""
    print(result)
    


if __name__ == "__main__":
    matrix = get_stack_2()
    # with open("help.txt", "w") as f:
    #     f.write(str(matrix))
    # resolve_operation(matrix)