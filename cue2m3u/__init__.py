from __future__ import annotations

from argparse import ArgumentParser
from os.path import basename, commonprefix
from pathlib import Path

__version__ = "0.1.0"


def main() -> None:
    parser = ArgumentParser(description="Generate playlists for disc-based games.")

    parser.add_argument(
        "input",
        help="The location of the games to generate playlists for.",
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Scan subfolders of `input`.",
    )

    args = parser.parse_args()

    paths = [Path(args.input)]
    while paths:
        path, *paths = paths

        cues: list[Path] = []

        for item in path.iterdir():
            if item.is_dir():
                if args.recursive:
                    paths.append(item)
                continue

            if item.suffix == ".m3u":
                cues = []
                break

            if item.suffix == ".cue":
                cues.append(item)

        if not cues:
            continue

        name = _find_common_prefix(cues)
        playlist = cues[0].with_name(name).with_suffix(".m3u")

        print(f"Generating {playlist}")
        with open(playlist, "w") as f:
            for cue in sorted(cues):
                f.write(f"{cue.name}\n")


def _find_common_prefix(paths: list[Path]) -> str:
    prefix = commonprefix(paths)
    prefix = basename(prefix)
    return _trim_trailing_characters(prefix)


def _trim_trailing_characters(s: str) -> str:
    # This is a very naive implementation. It assumes reasonable use of
    # parentheses in file names and can be tripped up by things like
    # multiple sets of unbalanced parentheses.
    last_open_index = s.rindex("(") if "(" in s else -1
    last_close_index = s.rindex(")") if ")" in s else -1
    if last_open_index > last_close_index:
        s = s[:last_open_index]
    return s.strip()
