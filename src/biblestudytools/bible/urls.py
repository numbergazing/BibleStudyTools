from .exceptions import check_bible_version_and_book_slug

_home = "https://www.biblestudytools.com"
_bible = _home + "/{version_code}"
_book = _bible + "/{book_slug}"
_chapter = _book + "/{chapter_num}.html"


def construct_book_url(bible_version: str, book_slug: str) -> str:

    bible_version_code: str

    bible_version_code = check_bible_version_and_book_slug(bible_version, book_slug)
    return _book.format(version_code=bible_version_code, book_slug=book_slug)


def construct_chapter_url(bible_version: str, book_slug: str, chapter_num: int) -> str:

    bible_version_code: str

    bible_version_code = check_bible_version_and_book_slug(bible_version, book_slug)
    # TODO Check if given chapter num isn't bigger than the available number of chapters

    return _chapter.format(version_code=bible_version_code, book_slug=book_slug, chapter_num=chapter_num)
