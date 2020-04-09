import pytest


test_set = set()


@pytest.fixture()
def fixture_for_update_set():
    test_set.update({1, 2, 3})
    return test_set


@pytest.fixture(params=["test", 10, True, (1, 2), 0])
def fixture_for_dictionary(request):
    return request.param
