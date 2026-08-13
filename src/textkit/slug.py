"""Turn arbitrary text into a URL-safe slug.

The one function in this package is deliberately left unimplemented: this repo is
the target of an automated graph-engineering run, and `slugify` is the goal it is
asked to fill in. The tests in `tests/test_slug.py` are the specification.
"""


def slugify(text: str) -> str:
    """Return a URL-safe slug for ``text``.

    See ``tests/test_slug.py`` for the exact behaviour this must satisfy.
    """
    raise NotImplementedError("slugify is the goal of this run")
