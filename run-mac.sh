#!/bin/sh
set -eu

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
make -s -C "$project_dir" >&2

# The existing engine loads TINY.BIN from its working directory.
cd "$project_dir/dos"
exec "$project_dir/build/tiny" "$@"
