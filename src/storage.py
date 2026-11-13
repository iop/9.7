"""Persist a NoteBook to a JSON file on disk."""

import json

from notes import NoteBook


def save(notebook, path):
    data = [vars(note) for note in notebook.list()]
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


def load(path):
    with open(path, encoding="utf-8") as fh:
        rows = json.load(fh)
    book = NoteBook()
    for row in rows:
        book.add(row["title"], row["body"], row.get("tags", []))
    return book


def load_or_empty(path):
    """Load notes from path, or return an empty NoteBook if it is missing."""
    import os

    if not os.path.exists(path):
        return NoteBook()
    return load(path)
