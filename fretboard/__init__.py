# Monkey patch collections
import collections
import collections.abc

for type_name in collections.abc.__all__:
    setattr(collections, type_name, getattr(collections.abc, type_name))
from .chord import BassChord, GuitarChord, UkuleleChord  # noqa: E402
from .fretboard import BassFretboard, GuitarFretboard, UkuleleFretboard  # noqa: E402

__version__ = "1.0.0"
__author__ = "Derek Payton <derek.payton@gmail.com>"
__license__ = "MIT"
