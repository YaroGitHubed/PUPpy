import math
from my_tests.pidentcomments import pident_comment, DEFAULT, PERFECT, IMPERFECT

def test_defaults_and_branches():
    assert "No alignment" in pident_comment(None, 3)
    assert "aligns perfectly" in pident_comment(100, 1)
    assert "does not align perfectly" in pident_comment(99.9, 1)
    # With 0 targets we fall back to DEFAULT
    assert "No alignment" in pident_comment(0, 0)

def test_never_raises_on_weird_inputs():
    for pair in [("x","y"), ([],{}), (object(),object()), (-1,-1)]:
        out = pident_comment(*pair)
        assert isinstance(out, str)
        assert "No alignment" in out

def test_constants_are_strings():
    for s in (DEFAULT, PERFECT, IMPERFECT):
        assert isinstance(s, str)


