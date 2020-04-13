import pytest


start_list = []


@pytest.mark.parametrize("expected_result", [[1, 2, 3]])
def test_extend_list(expected_result):
    start_list.extend([1, 2, 3])
    assert start_list == expected_result


@pytest.mark.parametrize("expected_result", [[2, 1, 2, 3]])
def test_insert_list(expected_result):
    start_list.insert(0, 2)
    assert start_list == expected_result


@pytest.mark.parametrize("expected_result", [[1, 2, 3]])
def test_remove_list(expected_result):
    start_list.remove(2)
    assert start_list == expected_result


@pytest.mark.parametrize("expected_result", [3])
def test_pop_list(expected_result):
    removed_element = start_list.pop()
    assert removed_element == expected_result


@pytest.mark.parametrize("expected_result", [[2, 1]])
def test_reverse_list(expected_result):
    start_list.reverse()
    assert start_list == expected_result
