"""The specification for ``slugify``, written as tests.

These pin the behaviour tightly enough that there is one right answer and many
ways to write it — which is what makes the parallel branches of a run actually
explore rather than converge on one phrasing.

The rules, stated once here and encoded below:

* lowercase everything
* a run of spaces or underscores becomes a single hyphen
* drop any character that is not ``a-z``, ``0-9`` or ``-``
* collapse repeated hyphens into one
* strip leading and trailing hyphens
"""

from textkit.slug import slugify


def test_basic_words_become_hyphenated():
    assert slugify("Hello World") == "hello-world"


def test_punctuation_is_dropped():
    assert slugify("Hello,  World!") == "hello-world"


def test_leading_and_trailing_whitespace_is_stripped():
    assert slugify("  Trailing spaces  ") == "trailing-spaces"


def test_underscores_and_spaces_both_become_hyphens():
    assert slugify("snake_case name") == "snake-case-name"


def test_digits_survive_and_symbols_do_not():
    assert slugify("Rooms: 101 & 202") == "rooms-101-202"


def test_an_existing_slug_is_unchanged():
    assert slugify("already-a-slug") == "already-a-slug"


def test_repeated_separators_collapse_to_one_hyphen():
    assert slugify("Mix___of---stuff") == "mix-of-stuff"


def test_empty_string_stays_empty():
    assert slugify("") == ""
