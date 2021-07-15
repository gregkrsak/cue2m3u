from __future__ import annotations

from argparse import ArgumentParser
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
            if item.is_dir() and args.recursive:
                paths.append(item)
                continue

            if item.suffix == ".m3u":
                cues = []
                break

            if item.suffix == ".cue":
                cues.append(item)

        if not cues:
            continue

        playlist = cues[0].with_suffix(".m3u")
        print(f"Generating {playlist}")
        with open(playlist, "w") as f:
            for cue in sorted(cues):
                f.write(f"{cue.name}\n")
