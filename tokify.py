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
    >>> a, b = tokens.float(2)

    """

    def __init__(self, stream=None):
        raw_stream = stream or stdin
        self.token_stream = self._token_stream(raw_stream)

    def str(self, amount=1):
        """Read string token(s)."""
        return self.token(amount=amount, convert_func=str)

    def float(self, amount=1):
        """Read float token(s)."""
        return self.token(amount=amount, convert_func=float)

    def int(self, amount=1):
        """Read int token(s)."""
        return self.token(amount=amount, convert_func=int)

    def token(self, amount=1, convert_func=str):
        """Read token(s), then apply convert_func."""
        tokens = tuple(map(convert_func, islice(self.token_stream, amount)))
        return tokens[0] if amount == 1 else tokens

    def _token_stream(self, stream):
        # Create a token generator from the stream.
        with closing(stream):
            for line in stream:
                for token in line.split():
                    yield token
