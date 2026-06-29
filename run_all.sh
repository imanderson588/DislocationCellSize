#!/usr/bin/env bash
set -euo pipefail

for dir in CellSize_*/; do
  [[ -d "$dir" ]] || continue
  echo "Running in $dir"
  (
    cd "$dir"
    sbatch run.sh
  )
done