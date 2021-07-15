from __future__ import annotations

from pathlib import Path, PurePath

import pytest

from cue2m3u import _find_common_prefix, _trim_trailing_characters


@pytest.mark.parametrize(
    ("expected", "paths"),
    (
        ("prefix", [PurePath("prefix")]),
        ("prefix", [PurePath("prefix"), PurePath("prefix2")]),
        ("prefix", [PurePath("prefix1"), PurePath("prefix2"), PurePath("prefix3")]),
        ("prefix", [PurePath("prefix (1)"), PurePath("prefix (2)")]),
    ),
)
def test_find_common_prefix(expected: str, paths: list[Path]) -> None:
    actual = _find_common_prefix(paths)
    assert actual == expected


@pytest.mark.parametrize("expected", ("()", "()()", "abc()", "(abc)", "()abc"))
def test_trim_trailing_whitespace_leaves_balanced_parentheses_intact(
    expected: str,
) -> None:
    actual = _trim_trailing_characters(expected)
    assert actual == expected


@pytest.mark.parametrize("expected", ("abc", "def", "abc def"))
def test_trim_trailing_whitespace_leaves_ordinary_names_intact(expected: str) -> None:
    actual = _trim_trailing_characters(expected)
    assert actual == expected


@pytest.mark.parametrize(
    ("initial", "expected"),
    (
        ("abc(", "abc"),
        ("(", ""),
        ("()(", "()"),
    ),
)
def test_trim_trailing_whitespace_removes_unbalanced_parentheses(
    initial: str, expected: str
) -> None:
    actual = _trim_trailing_characters(initial)
    assert actual == expected


@pytest.mark.parametrize(
    ("initial", "expected"),
    (
        ("abc ", "abc"),
        ("abc  ", "abc"),
        ("abc   ", "abc"),
        (" abc ", "abc"),
        (" abc", "abc"),
    ),
)
def test_trim_trailing_characters_removes_whitespace(
    initial: str, expected: str
) -> None:
    actual = _trim_trailing_characters(initial)
    assert actual == expected
