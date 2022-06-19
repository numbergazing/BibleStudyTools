import pytest

from biblestudytools.bible.exceptions import BibleVersionDoesNotExistError, BookDoesNotExistError
from biblestudytools.bible.urls import construct_chapter_url


def test_construct_chapter_url():
    expected_result = [
        "https://www.biblestudytools.com/lxx/esther/9.html",
        "https://www.biblestudytools.com/kjv/1-chronicles/24.html",
        "https://www.biblestudytools.com/kjv/2-timothy/2.html",
    ]
    result = [
        construct_chapter_url("septuagint", "esther", 9),
        construct_chapter_url("king-james", "1-chronicles", 24),
        construct_chapter_url("king-james", "2-timothy", 2),
    ]
    assert result == expected_result


def test_not_construct_chapter_url():
    with pytest.raises(BibleVersionDoesNotExistError):
        construct_chapter_url("foo", "esther", 9)
    with pytest.raises(BookDoesNotExistError):
        construct_chapter_url("king-james", "bar", 24),
