import re


RE_JSON_KEY = re.compile(r'''
    "(?P<key>[^"]*)"  # Key
    :\s*  # Separator
    # "(?P<value>(?:\"|.)*?)"
    "(?P<value>[^"]*)"  # Value
''', re.X)


class Parser:
    """
    The main parser class
    """

    def __init__(self, content):
        """
        Build a catalog of useful data from content
        """
        # Collect results extracted as JSON
        self._json_cache = [
            match.groups()
            for match in RE_JSON_KEY.finditer(content)
        ]

    def first(self, key):
        """
        Find the first occurence of "key"
        """
        # Look through the JSON cache
        for name, value in self._json_cache:
            if key == name:
                return value

        # Exhaustion
        else:
            return None
