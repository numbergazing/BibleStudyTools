from biblestudytools.bible.nav import get_book_size


def test_get_book_size():
    expected_result = [50, 66, 5]
    result = [
        get_book_size("septuagint", "genesis"),
        get_book_size("king-james", "isaiah"),
        get_book_size("king-james", "james"),
    ]
    assert result == expected_result
