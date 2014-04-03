from sys import stdin
from itertools import islice
from contextlib import closing

class Tokifier:
    """Read whitespace-separated tokens from a stream.

    By default, Tokifier reads from standard input (or a file specified by
    argv[1]). Alternatively, pass the constructer a file object to read from a
    different stream.

    >>> import tokify
    >>> tokens = tokify.Tokifier()
    >>> x = tokens.int()
    >>> a, b = tokens.floats(2)

    """

    def __init__(self, stream=None):
        raw_stream = stream or stdin
        self.token_stream = self._token_stream(raw_stream)

    def str(self):
        """Read string token."""
        return next(self.token_stream)

    def strs(self, amount):
        """Read string tokens."""
        return [self.str() for _ in range(amount)]

    def int(self):
        """Read int token."""
        return int(self.str())

    def ints(self, amount):
        """Read int tokens."""
        return [int(tok) for tok in self.strs(amount)]

    def float(self):
        """Read float token."""
        return float(self.str())

    def floats(self, amount):
        """Read float tokens."""
        return [float(tok) for tok in self.strs(amount)]

    def _token_stream(self, stream):
        # Create a token generator from the stream.
        with closing(stream):
            for line in stream:
                for token in line.split():
                    yield token
