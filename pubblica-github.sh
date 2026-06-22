#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git init
  git branch -M main
fi

git add .
git commit -m "Sito portfolio Stefano Davide Ciancimino" || true
git push -u origin main

echo "Deploy avviato su GitHub Pages."
echo "Repo: https://github.com/SatoshiAllien/Stefano"