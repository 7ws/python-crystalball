import pytest

import crystalball


@pytest.mark.parametrize('json_text', [
    '{"foo": "bar"}',  # Normal JSON
    '[{"foo": "bar"}]',  # Object within a list
    '{"baz": {"foo": "bar"},}',  # Object within another
])
def test_finds_json_keys(json_text):
    """
    Values can be extracted from JSON-like documents
    """
    cb = crystalball.parse(json_text)
    assert cb.first('foo') == 'bar'
