__all__ = ["construct_chapter_url"]

from sys import exit

from .util import bible_versions, bible_version_codes, version_books
from .exceptions import BibleVersionDoesNotExistError, BookDoesNotExistError

_home = "https://www.biblestudytools.com"
_bible = _home + "/{version_code}"
_book = _bible + "/{book_slug}"
_chapter = _book + "/{chapter_num}.html"


def construct_chapter_url(bible_version: str, book_slug: str, chapter_num: int) -> str:

    bible_version_code: str

    if bible_version not in bible_versions.keys():
        raise BibleVersionDoesNotExistError

    try:
        bible_version_code = bible_version_codes[bible_version]
        this_version_books = version_books[bible_version]

        if book_slug not in this_version_books:
            raise BookDoesNotExistError

        # TODO Check if given chapter num isn't bigger than the available number of chapters

    except ValueError:
        print("An existing Bible version has no code or assigned books.")
        exit(1)
    else:
        return _chapter.format(version_code=bible_version_code, book_slug=book_slug, chapter_num=chapter_num)
