import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE, delimiter=",", new_line="\n"):
    f = open(INPUT_FILE)
    num_of_elements = []
    values = []
    while True:
        # считываем строку
        line = f.readline()
        value = ""
        num = 0
        for i in range(len(line)):
            if line[i] == new_line:
                values.append(value)
                num+=1
                value = ""
            elif line[i] != delimiter:
                value+= line[i]
            else:
                values.append(value)
                num += 1
                value = ""
        num_of_elements.append(num)

        # прерываем цикл, если строка пустая
        if not line:
            break

    # Создаем список ключей
    keys = [values.pop(0) for i in range(num_of_elements[0])]
    result = []
    # Создаем список значений
    for i in range(0, int(len(values)), 3):
        tmp_dict = {}
        tmp_dict[keys[0]] = values[i]
        tmp_dict[keys[1]] = values[i+1]
        tmp_dict[keys[2]] = values[i+2]
        result.append(tmp_dict)
    return result





csv_to_list_dict(INPUT_FILE)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
