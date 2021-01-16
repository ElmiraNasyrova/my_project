import pytest

menu_set = {'coffee', 'smoothies', 'tea', 'porridge'}


def test_add_new_item_to_set():
    added_item = "juice"
    menu_set.add(added_item)
    assert added_item in menu_set


def test_convert_list_to_set():
    menu_list = ['pizza', 'pasta', 'burger', 'coca-cola']
    menu_list = set(menu_list)
    assert type(menu_list) is set


@pytest.mark.parametrize("subset",
                         [{'coffee'}, {'smoothies'}, {'tea', 'porridge'}])
def test_issubset(subset):
    assert subset.issubset(menu_set)


def test_difference_sets():
    new_set=set('efdf')
    new_set_2 = set('adwwed')
    assert menu_set.difference(new_set, new_set_2)


def test_remove_element_from_set():
    length_before_remove = len(menu_set)
    menu_set.remove('tea')
    assert len(menu_set) < length_before_remove
