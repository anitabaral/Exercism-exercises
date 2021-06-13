def extract_columns(list, i):
    return [item[i] for item in list]

def saddle_points(matrix):
    points = []
    if len(set(map(len, matrix))) > 1:
        raise ValueError('Irregular shape')
    for i, row in enumerate(matrix):
        for j, number in enumerate(row):
            if number == max(row) and number == min(extract_columns(matrix, j)):
                points.append({"row" : i + 1, "column": j+1})

    return points
