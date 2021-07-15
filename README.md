# cue2m3u

Generate playlists for disc-based games.

## Installation

[Poetry] is required to use this tool. It is available through most package
managers. For example, to install it with [pip], use

```
$ pip install poetry
```

After [poetry] has been installed, the script's requirements can be installed by
running

```
$ poetry install
```

## Usage

To generate playlists, use the `generate` [poetry] script. For detailed
information, run

```
$ poetry run generate --help
```

## Development

### Code style

This code base uses [pre-commit] to control apply stylistic restraints. If you
have it installed globally, [pre-commit] will automatically run whenever you
create a new commit.

There are no additional style restrictions on the code.

[pip]: https://pip.pypa.io
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
