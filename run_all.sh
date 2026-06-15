#!/usr/bin/env bash
set -euo pipefail

for dir in */; do
  [[ -d "$dir" ]] || continue
  echo "Running in $dir"
  (
    cd "$dir"
    sbatch run.sh
  )
done