#!/bin/sh

set -e

# Activate our virtual environment here.
. /opt/pysetup/.venv/bin/activate

# Additional setup logic may go below.

# Evaluate passed docker command.
exec "$@"
