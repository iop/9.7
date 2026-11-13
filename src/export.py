"""Export a notebook to a JSON string (no file needed)."""

import json


def to_json(book):
    return json.dumps([vars(n) for n in book.list()], indent=2)
