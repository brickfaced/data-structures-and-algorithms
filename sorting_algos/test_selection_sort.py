from selection_sort import selection_sort


def test_small_lst(small_lst):
    assert selection_sort(small_lst) == [1]


def test_uneven_lst(uneven_lst):
    assert selection_sort(uneven_lst) == [7, 11, 24, 30, 72, 100]


def test_reversed_list(reversed_lst):
        assert selection_sort(reversed_lst) == [1, 2, 3, 4, 5]
