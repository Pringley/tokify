# Tokify

Read whitespace-separated tokens from a stream.

By default, Tokifier reads from standard input (or a file specified by
argv[1]). Alternatively, pass the constructer a file object to read from a
different stream.

```python
>>> import tokify
>>> x = tokify.int()
>>> a, b = tokify.floats(2)
```

## Install

To install, clone the repository, then run `setup.py`:

    git clone https://github.com/Pringley/tokify
    cd tokify
    python setup.py install

The last command may require administrative privileges or `sudo`.
