import pytest

from biblestudytools.bible.exceptions import VerseDoesNotExistError
from biblestudytools.bible.nav import get_verses, get_verse
from biblestudytools.bible.util import Verse


def test_get_verses():

    expected_result = [
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 1,
            "text": "In the beginning God made the heaven and the earth."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 2,
            "text": "But the earth was unsightly and unfurnished, and darkness was over the deep, and the Spirit of God moved over the water."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 3,
            "text": "And God said, Let there be light, and there was light."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 4,
            "text": "And God saw the light that it was good, and God divided between the light[a] and the darkness."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 5,
            "text": "And God called the light Day, and the darkness he called Night, and there was evening and there was morning, the first day."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 6,
            "text": "And God said, Let there be a firmament in the midst of the water, and let it be a division between water and water, and it was so."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 7,
            "text": "And God made the firmament, and God divided between the water which was under the firmament and the water which was above the firmament."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 8,
            "text": "And God called the firmament Heaven, and God saw that it was good, and there was evening and there was morning, the second day."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 9,
            "text": "And God said, Let the water which is under the heaven be collected into one[b] place, and let the dry land appear, and it was so. And the water which was under the heaven was collected into its places,[c] and the dry land appeared."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 10,
            "text": "And God called the dry land Earth, and the[d] gatherings of the waters he called Seas, and God saw that it was good."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 11,
            "text": "And God said, Let the earth bring forth the herb of grass[e] bearing seed according to its kind[f] and according to its likeness, and the fruit-tree bearing fruit whose seed is in it, according to its kind on the earth, and it was so."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 12,
            "text": "And the earth brought forth the herb of grass bearing seed according to its kind and according to its likeness, and the fruit tree bearing fruit whose seed is in it, according to its kind on the earth, and God saw that it was good."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 13,
            "text": "And there was evening and there was morning, the third day."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 14,
            "text": "And God said, Let there be lights in the firmament of the heaven[g] to give light upon the earth, to divide between day and night, and let them be for signs and for seasons and for days and for years."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 15,
            "text": "And let them be for light in the firmament of the heaven, so as to shine upon the earth, and it was so."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 16,
            "text": "And God made the two great lights, the greater light for regulating the day and the lesser light for regulating the night, the stars also."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 17,
            "text": "And God placed them in the firmament of the heaven, so as to shine upon the earth,"
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 18,
            "text": "and to regulate day and night, and to divide between the light and the darkness. And God saw that it was good."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 19,
            "text": "And there was evening and there was morning, the fourth day."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 20,
            "text": "And God said, Let the waters bring forth reptiles[h] having life, and winged creatures flying above the earth in the firmament of heaven, and it was so."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 21,
            "text": "And God made great[i] whales, and[j] every living reptile, which the waters brought forth according to their kinds, and every creature that flies with wings according to its kind, and God saw that they were good."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 22,
            "text": "And God blessed them saying, Increase and multiply and fill the waters in the seas, and let the creatures that fly be multiplied on the earth."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 23,
            "text": "And there was evening and there was morning, the fifth day."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 24,
            "text": "And God said, Let the earth bring forth the living[k] creature according to its kind, quadrupeds and reptiles and wild beasts of the earth according to their kind, and it was so."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 25,
            "text": "And God made the wild beasts of the earth according to their kind, and cattle according to their kind, and all the reptiles of the earth according to their kind, and God saw that they were good."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 26,
            "text": "And God said, Let us make man according to our image and likeness, and let them have dominion over the fish of the sea, and over the flying creatures of heaven, and over the cattle and all the earth, and over all the reptiles that creep on the earth."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 27,
            "text": "And God made man, according to the image of God he made him, male and female he made them."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 28,
            "text": "And God blessed them, saying, Increase and multiply, and fill the earth and subdue it, and have dominion over the fish of the seas and flying creatures of heaven, and all the cattle and all the earth, and all the reptiles that creep on the earth."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 29,
            "text": "And God said, Behold I have given to you every seed-bearing herb sowing seed which is upon all the earth, and every tree which has in itself the fruit of seed that is sown, to you it shall be for food."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 30,
            "text": "And to all the wild beasts of the earth, and to all the flying creatures of heaven, and to every reptile creeping on the earth, which has in itself the[l] breath of life, even every green plant for food; and it was so."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 31,
            "text": "And God saw all the things that he had made, and, behold, they were very good. And there was evening and there was morning, the sixth day."
        }
    ]
    result = get_verses("septuagint", "genesis", 1)
    assert [row.__dict__ for row in result] == expected_result

    expected_result = [
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 1,
            "text": "In the beginning God made the heaven and the earth."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 2,
            "text": "But the earth was unsightly and unfurnished, and darkness was over the deep, and the Spirit of God moved over the water."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 3,
            "text": "And God said, Let there be light, and there was light."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 4,
            "text": "And God saw the light that it was good, and God divided between the light[a] and the darkness."
        },
        {
            "bible_version": "Septuagint",
            "book": "Genesis",
            "chapter_num": 1,
            "verse_num": 5,
            "text": "And God called the light Day, and the darkness he called Night, and there was evening and there was morning, the first day."
        }
    ]
    result = get_verses("septuagint", "genesis", 1, first=1, last=5)
    assert [row.__dict__ for row in result] == expected_result


def test_not_get_verses():

    with pytest.raises(VerseDoesNotExistError):
        get_verses("septuagint", "genesis", 1, first=1, last=420)

    with pytest.raises(ValueError):
        get_verses("septuagint", "genesis", 1, first=6, last=5)


def test_get_verse():
    expected_result = Verse(
        bible_version='Septuagint',
        book='Genesis',
        chapter_num=1,
        verse_num=1,
        text='In the beginning God made the heaven and the earth.'
    )
    result = get_verse("septuagint", "genesis", 1, 1)
    assert result == expected_result


def test_not_get_verse():
    with pytest.raises(VerseDoesNotExistError):
        get_verse("septuagint", "genesis", 1, 420)
