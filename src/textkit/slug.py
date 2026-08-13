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
    # Lowercase everything
    text = text.lower()
    
    # Replace runs of spaces or underscores with a single hyphen
    result = []
    prev_was_space_or_underscore = False
    for char in text:
        if char in (' ', '_'):
            if not prev_was_space_or_underscore:
                result.append('-')
            prev_was_space_or_underscore = True
        else:
            prev_was_space_or_underscore = False
            result.append(char)
    
    text = ''.join(result)
    
    # Drop any character that is not a-z, 0-9, or a hyphen
    text = ''.join(char for char in text if char.isalnum() or char == '-')
    
    # Collapse repeated hyphens into one
    while '--' in text:
        text = text.replace('--', '-')
    
    # Strip leading and trailing hyphens
    text = text.strip('-')
    
    return text