from table import column_sums, diagonal_pattern, row_sums, transform


def test_sums_and_patterns():
    m1 = [[1, 2, 3], [4, 5, 6]]
    assert row_sums(m1) == [6, 15]
    assert column_sums(m1) == [5, 7, 9]

    m2 = [[7]]
    assert row_sums(m2) == [7]
    assert column_sums(m2) == [7]
    assert diagonal_pattern(1) == [[0]]

    m3 = [[1], [-1], [0]]
    assert row_sums(m3) == [1, -1, 0]
    assert column_sums(m3) == [0]

    assert row_sums([]) == []
    assert column_sums([]) == []
    assert transform([]) == []

    assert diagonal_pattern(3) == [
        [0, 1, 1],
        [2, 0, 1],
        [2, 2, 0],
    ]


def test_variant_14_and_immutability():
    control = [[-2, 0, 3], [4, -5, 6]]
    snapshot = [row.copy() for row in control]

    result = transform(control)
    assert result == [[4, 0, 9], [4, -5, 6]]
    assert control == snapshot

    result[0][0] = 999
    assert control == snapshot
    assert control[0][0] == -2


if __name__ == "__main__":
    test_sums_and_patterns()
    test_variant_14_and_immutability()
    print("Все проверки пройдены успешно.")