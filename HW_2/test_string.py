import pytest


@pytest.mark.parametrize("input_string, result_string", [("a12b".isalnum(), True),
                                                         ("ab".islower(), True),
                                                         ("12,a".isdecimal(), False),
                                                         ("   ".isspace(), True),
                                                         ("test".istitle(), False)])
def test_string_methods(input_string, result_string):
    assert input_string == result_string
