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
    # Replace runs of spaces and underscores with a placeholder
    result = text.lower()
    
    # Use a two-pass approach: first mark boundaries, then clean
    chars = []
    prev_was_separator = False
    
    for char in result:
        if char in (' ', '_'):
            if not prev_was_separator:
                chars.append('-')
                prev_was_separator = True
        elif char.isalnum() or char == '-':
            chars.append(char)
            prev_was_separator = False
        else:
            prev_was_separator = False
    
    # Join and collapse repeated hyphens
    result = ''.join(chars)
    while '--' in result:
        result = result.replace('--', '-')
    
    # Strip leading and trailing hyphens
    return result.strip('-')