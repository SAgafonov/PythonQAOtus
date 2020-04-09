
def test_dict_method_values(fixture_for_dictionary):
    test_dict = {"val_1": "test", "val_2": 10, "val_3": True, "val_4": (1, 2), "val_5": 0}
    assert fixture_for_dictionary in test_dict.values()
