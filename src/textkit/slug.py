"""Turn arbitrary text into a URL-safe slug.

The one function in this package is deliberately left unimplemented: this repo is
the target of an automated graph-engineering run, and `slugify` is the goal it is
asked to fill in. The tests in `tests/test_slug.py` are the specification.
"""


def slugify(text: str) -> str:
    """Return a URL-safe slug for ``text``.

    Converts text to lowercase, replaces runs of spaces/underscores with hyphens,
    removes non-alphanumeric characters (except hyphens), collapses repeated hyphens,
    and strips leading/trailing hyphens.
    """
    # Lowercase
    text = text.lower()
    
    # Replace runs of spaces or underscores with a single hyphen
    result = []
    in_separator = False
    for char in text:
        if char in (' ', '_'):
            if not in_separator:
                result.append('-')
                in_separator = True
        else:
            in_separator = False
            # Keep only a-z, 0-9, and hyphens
            if char.isalnum() or char == '-':
                result.append(char)
    
    # Join and collapse repeated hyphens
    slug = ''.join(result)
    while '--' in slug:
        slug = slug.replace('--', '-')
    
    # Strip leading and trailing hyphens
    slug = slug.strip('-')
    
    return slug