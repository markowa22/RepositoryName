list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_1 = 0

for m in range(len(list_numbers)):
    max_numbers = list_numbers[max_1]
    current_n = list_numbers[m]
    if current_n > max_numbers:
        max_1 = m

list_numbers[max_1], list_numbers[-1] = list_numbers[-1], list_numbers[max_1]

print(list_numbers)
