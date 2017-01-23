import io

from . import parser


def parse(something):
    """
    A shortcut to the main parser class
    """
    # Check if we have a file-like object
    if isinstance(something, io.IOBase):
        content = something.read()

    # Fallback to the original value
    else:
        content = something

    return parser.Parser(content=content)
