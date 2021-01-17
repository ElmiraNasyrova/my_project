import pytest

string_data = 'imaginary fruit'


@pytest.mark.parametrize("test_data",
                         ['test', 'apple is fruit', 'dsfsdf', '21323'])
def test_type(test_data):
    assert type(test_data) is str


def test_replace_letters():
    replaced_string =string_data.replace('i', 'y')
    assert replaced_string != string_data


def test_concatenation():
    new_word = 'apple'
    concatenated_string = string_data + ' is ' + new_word
    assert new_word in concatenated_string


@pytest.mark.xfail()
def test_find_letter():
    assert string_data.find('qqqq')


def test_remove_first_word():
    words = string_data.split(' ')
    length_first_word = len(words[0])
    string_data_after_remove = string_data[length_first_word:]
    string_data_after_remove = string_data_after_remove.replace(' ', '')

    assert string_data_after_remove == words[1]
