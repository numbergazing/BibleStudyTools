from re import compile

from bs4 import BeautifulSoup, ResultSet

from biblestudytools.bible.urls import construct_book_url
from biblestudytools.nav import get_markup


def get_book_size(bible_version: str, book_slug: str) -> int:

    url: str
    html: BeautifulSoup
    links: ResultSet

    url = construct_book_url(bible_version, book_slug)
    html = get_markup(url)
    links = html.find_all(href=compile(url + r"/\d+\.html"))

    return len(links)
