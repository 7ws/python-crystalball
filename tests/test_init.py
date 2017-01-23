from unittest import mock
import io

import crystalball as cb


class TestParse:

    def test_shortcut_initializes_parser_with_file_pointer(self):
        """
        The main Parser shortcut initializes it with a file object
        """
        file_obj = io.StringIO('foo=bar')
        with mock.patch('crystalball.parser.Parser') as Parser:
            cb.parse(file_obj)
        assert Parser.call_args == mock.call(content='foo=bar')

    def test_shortcut_initializes_parser_with_text(self):
        """
        The main Parser shortcut initializes it with text
        """
        text = 'foo=bar'
        with mock.patch('crystalball.parser.Parser') as Parser:
            cb.parse(text)
        assert Parser.call_args == mock.call(content='foo=bar')
