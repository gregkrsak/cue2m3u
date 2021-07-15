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

### Testing

Testing is controlled via [tox]. If you wish to invoke it directly, it is
installed as a development dependency by [poetry] and can be invoked with

```
$ poetry run tox
```

To have [tox] only perform static type checking of the code run

```
$ poetry run tox -e types
```

To run just the unit tests, use

```
$ poetry run tox -e unit
```

### CI

While the local use of both [pre-commit] and [tox] are encouraged, it is not
required. Both style and test enforcement will be run as part of CI on [GitHub
Actions][actions].

**NOTE:** CI will not update the pull request with changes made by [pre-commit].
You will need to add these to your code yourself.

[actions]: https://docs.github.com/en/actions
[pip]: https://pip.pypa.io
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
[tox]: https://tox.readthedocs.io
