# Crystal Ball

A Python library to guess and extract data from inconsistent structures.

This project intends to help on cases that require reading and parsing
text without a stable structural organization in order to extract
valuable data from it.

For example, consider the JSON document below and assume you don't know
where a possible domain name is.

```json
[
    {"origin": "somewhere", "domain": "foo.example.com"},
    {"origin": "somewhere", "extra_data": "domain=bar.example.com"},
]
```

Now let's parse it through crystalball and try out some extraction:

```python
>>> import crystalball
>>> cb = crystalball.parse(open('weird_stuff.json', 'r'))
>>> cb.findall('domain')
[Match('foo.example.com'), Match('bar.example.com')]
```

Any `Match` object will contain all the strategy used to acquire the
value in the document, such as the key hierarchy it went through and
additional parsing it had to perform.

Learn more at the documentation (TODO).
