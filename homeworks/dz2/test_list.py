import pytest

menu_list = ['pizza', 'pasta', 'burger', 'coca-cola']
menu_set = {'coffee', 'smoothies', 'tea', 'porridge'}


@pytest.mark.parametrize("new_item",
                         ['juice', 'swatch', menu_list[1], 2321])
def test_add_new_item_to_list(new_item):
    menu_list.append(new_item)
    assert menu_list[len(menu_list)-1] == new_item


def test_remove_item_from_list():
    removed_item = menu_list.pop(0)
    assert removed_item not in menu_list


def test_revers_list():
    original_menu = menu_list.copy()
    menu_list.reverse()
    for i in range(len(menu_list)):
        assert original_menu[i] == menu_list[len(menu_list)-i-1]


def test_extend_list():
    menu_list.extend(menu_set)
    assert type(menu_list) is list


def test_clear_list():
    menu_list.clear()
    assert menu_list == []
