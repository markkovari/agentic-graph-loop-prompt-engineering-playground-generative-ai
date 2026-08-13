# textkit

A deliberately tiny Python library that serves as the target for an automated
**graph-engineering run** built on [comp](https://github.com/markkovari/experiments).

## The idea

`src/textkit/slug.py` holds one unimplemented function, `slugify`. The tests in
`tests/test_slug.py` are its full specification. A run of the graph engine fans
out into several parallel *branches*, each asking a language model to implement
the function; every candidate is judged by actually running the tests; the branch
that passes them — smallest change, cheapest run — is opened as a pull request.

The human writes the goal and the tests. The machine writes the function and the
pull request. Nothing lands without the tests passing.

## Running the tests yourself

```bash
python -m pytest -q
```

On a fresh checkout these fail, because `slugify` raises `NotImplementedError`.
That is the point: the run's job is to make them pass.
