#!/usr/bin/env bash
BASE_PATH="$HOME/src/external/catalysis"
source "$BASE_PATH/.venv/bin/activate"
(cd "$BASE_PATH" && python3 ./catalysis.py)
