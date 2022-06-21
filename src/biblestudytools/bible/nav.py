from bs4 import BeautifulSoup, ResultSet

from biblestudytools.bible.urls import construct_chapter_url
from biblestudytools.bible.util import bible_versions, version_books, chain_replace, Verse
from biblestudytools.nav import get_markup


def get_verses(bible_version: str, book_slug: str, chapter_num: int) -> list[dict]:

    url: str
    html: BeautifulSoup
    divs: ResultSet
    filtered_divs: list

    url = construct_chapter_url(bible_version, book_slug, chapter_num)
    html = get_markup(url)
    divs = html.find_all("div")
    filtered_divs = [div for div in divs if "data-verse-id" in div.attrs.keys()]

    return [
        {
            "bible_version": bible_versions[bible_version],
            "book": version_books[bible_version][book_slug],
            "chapter_num": chapter_num,
            "verse_num": int(div.a.text),
            "text": chain_replace(div.text, ["\n", f"{int(div.a.text)}"], "").strip()
        }
        for div in filtered_divs
    ]


def get_verse(bible_version: str, book_slug: str, chapter_num: int, verse_num: int) -> Verse:

    url: str
    html: BeautifulSoup
    filtered_divs: list

    url = construct_chapter_url(bible_version, book_slug, chapter_num)
    html = get_markup(url)
    div = html.find("div", attrs={"data-verse-id": verse_num})

    return Verse(
        bible_versions[bible_version],
        version_books[bible_version][book_slug],
        chapter_num,
        verse_num,
        chain_replace(div.text, ["\n", f"{int(div.a.text)}"], "").strip(),
    )
