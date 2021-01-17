import pytest

menu = {
    "coffee": [{
        "name": 'latte',
        "price": 99,
        "volume": 0.4,
        "milk": True
    }, {
        "name": "espresso",
        "price": 45,
        "volume": 0.1,
        "milk": False
    }],
    "ice cream": "vanilla",
    "other": {
        "pizza", "pasta", "porridge"
    }
}


@pytest.mark.parametrize("test_data, type_of_data",
                         [(menu, dict),
                          (menu["coffee"], list),
                          (menu["coffee"][0], dict),
                          (menu["other"], set)])
def test_type(test_data, type_of_data):
    assert type(test_data) is type_of_data


def test_update_dict_item():
    menu.update({"other": "ice cream"})
    assert menu["other"] == "ice cream"


def test_add_dict_item():
    menu.update({"juice": "orange"})
    assert "juice" in menu.keys()


@pytest.mark.parametrize("test_data",
                         [menu, menu["coffee"][0]])
def test_dict_length(test_data):
    assert len(test_data.keys()) == len(test_data)


def test_remove_dict_item():
    menu.pop("ice cream")
    assert "ice cream" not in menu.keys()
