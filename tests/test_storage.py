"""Round-trip check for storage.save / storage.load."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import storage  # noqa: E402
from notes import NoteBook  # noqa: E402


def test_round_trip(tmp_path):
    book = NoteBook()
    book.add("hello", "world", ["greeting"])
    path = tmp_path / "notes.json"
    storage.save(book, path)
    again = storage.load(path)
    assert again.list()[0].title == "hello"
