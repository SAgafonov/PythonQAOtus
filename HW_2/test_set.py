import pytest


def test_update_set(fixture_for_update_set):
    assert fixture_for_update_set == {1, 2, 3}


def test_copy_set():
    original_set = {1, 2, 3}
    copied_set = original_set.copy()
    assert original_set == copied_set


def test_discard_set():
    test_set = {1, 2, 3, 4, 5, 6}
    test_set.discard(2)
    assert test_set == {1, 3, 4, 5, 6}


@pytest.mark.parametrize("input_set, main_set", [({1, 2}, {1, 2, 3})])
def test_issubset_set(input_set, main_set):
    assert input_set.issubset(main_set)


@pytest.mark.parametrize("input_set, expected_result", [({4, 5}, {1, 2, 3, 4, 5})])
def test_union_set(input_set, expected_result):
    test_set = {1, 2, 3}
    assert test_set.union(input_set) == expected_result
