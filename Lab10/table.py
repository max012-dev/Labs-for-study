def row_sums(matrix: list[list[int]]) -> list[int]:
    if not matrix:
        return []
    return [sum(row) for row in matrix]


def column_sums(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []
    num_cols = len(matrix[0])
    totals = [0] * num_cols
    for row in matrix:
        for col_idx in range(num_cols):
            totals[col_idx] += row[col_idx]
    return totals


def diagonal_pattern(size: int) -> list[list[int]]:
    if size < 1:
        raise ValueError("Размер таблицы должен быть целым числом не меньше 1")

    pattern: list[list[int]] = []
    for row in range(size):
        current_row: list[int] = []
        for column in range(size):
            if row == column:
                current_row.append(0)
            elif row < column:
                current_row.append(1)
            else:
                current_row.append(2)
        pattern.append(current_row)
    return pattern


def transform(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []

    result: list[list[int]] = []
    for row in matrix:
        new_row: list[int] = []
        for value in row:
            if -2 <= value <= 3:
                new_row.append(value * value)
            else:
                new_row.append(value)
        result.append(new_row)
    return result