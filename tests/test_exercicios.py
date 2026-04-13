def test_sort_two(io):
    assert io("exercicios.fs", ["1 2 sort-two"]).stack == [1, 2]
    assert io("exercicios.fs", ["2 1 sort-two"]).stack == [1, 2]
    assert io("exercicios.fs", ["3 2 1 sort-two"]).stack == [3, 1, 2]


def test_sort_three(io):
    assert io("exercicios.fs", ["1 2 3 sort-three"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["2 1 3 sort-three"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["3 2 1 sort-three"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["4 3 2 1 sort-three"]).stack == [4, 1, 2, 3]


def test_dots(io):
    assert "".join(io("exercicios.fs", ["3 dots"]).output) == "..."
    assert "".join(io("exercicios.fs", ["4 dots"]).output) == "...."


def test_power(io):
    assert io("exercicios.fs", ["2 3 **"]).stack == [8]
    assert io("exercicios.fs", ["5 0 **"]).stack == [1]
    assert io("exercicios.fs", ["2 10 **"]).stack == [1024]


def test_3dup(io):
    assert io("exercicios.fs", ["1 2 3 3dup"]).stack == [1, 2, 3, 1, 2, 3]
    assert io("exercicios.fs", ["1 2 3 4 5 6 3dup"]).stack == [1, 2, 3, 4, 5, 6, 4, 5, 6]


def test_put(io):
    assert io("exercicios.fs", ["1 2 3 42 2 put"]).stack == [1, 42, 2, 3]
    assert io("exercicios.fs", ["1 2 3 42 0 put"]).stack == [1, 2, 3, 42]


def test_reverse(io):
    assert io("exercicios.fs", ["10 20 30 3 reverse"]).stack == [30, 20, 10]
    assert io("exercicios.fs", ["0 10 20 30 3 reverse"]).stack == [0, 30, 20, 10]
    assert io("exercicios.fs", ["1 2 0 reverse"]).stack == [1, 2]


def test_drop_many(io):
    assert io("exercicios.fs", ["1 2 3 4 2 drop-many"]).stack == [1, 2]
    assert io("exercicios.fs", ["1 2 3 0 drop-many"]).stack == [1, 2, 3]


def test_drop_at(io):
    assert io("exercicios.fs", ["1 2 3 1 drop-at"]).stack == [1, 3]
    assert io("exercicios.fs", ["1 2 3 4 2 drop-at"]).stack == [1, 3, 4]
    assert io("exercicios.fs", ["1 2 3 4 0 drop-at"]).stack == [1, 2, 3]


def test_pop_at(io):
    assert io("exercicios.fs", ["1 2 3 4 2 pop-at"]).stack == [1, 3, 4, 2]
    assert io("exercicios.fs", ["1 2 3 0 pop-at"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["1 2 3 1 pop-at"]).stack == [1, 3, 2]


def test_print_change(io):
    result = io("exercicios.fs", ["42 print-change"]).lines
    assert result == [
        "0 nota(s) de 100",
        "0 nota(s) de 50",
        "2 nota(s) de 20",
        "0 nota(s) de 10",
        "0 nota(s) de 5",
        "1 nota(s) de 2",
        "0 moeda(s) de 1",
    ]


def test_max_n(io):
    assert io("exercicios.fs", ["10 42 -1 20 4 max-n"]).stack == [42]
    assert io("exercicios.fs", ["10 42 -1 20 10 2 4 max-n"]).stack == [10, 42, 20]
    assert io("exercicios.fs", ["10 1 max-n"]).stack == [10]


def test_reset(io):
    assert io("exercicios.fs", ["1 2 3 reset"]).stack == []
    assert io("exercicios.fs", ["1 2 3 4 reset"]).stack == []


def test_all_positive(io):
    assert io("exercicios.fs", ["1 2 3 all-positive"]).stack == [-1]
    assert io("exercicios.fs", ["all-positive"]).stack == [-1]
    assert io("exercicios.fs", ["1 -1 2 all-positive"]).stack == [0]


def test_all_sorted(io):
    assert io("exercicios.fs", ["1 2 3 all-sorted"]).stack == [-1]
    assert io("exercicios.fs", ["1 3 2 all-sorted"]).stack == [0]
    assert io("exercicios.fs", ["all-sorted"]).stack == [-1]


def test_filter_positive(io):
    assert io("exercicios.fs", ["1 2 3 filter-positive"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["-1 0 2 -3 4 filter-positive"]).stack == [0, 2, 4]