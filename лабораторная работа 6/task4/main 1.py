import json

filename = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='ln'):
    with open(filename) as f:
        dict = []
        for j, line in enumerate(f):
            fields = line.strip(new_line).split(delimiter)
            if j == 0:
                heads = fields
                continue

            dict.append({})

            for j, _ in enumerate(heads):

                dict[-1][heads[j]] = fields [j]
    return dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
