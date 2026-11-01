#!/usr/bin/env bash
set -euo pipefail

echo "==> Building Python image"
docker compose build python

echo "==> Starting Python container"
HOST_UID="$(id -u)" HOST_GID="$(id -g)" docker compose up --remove-orphans -d python

if [ "$#" -eq 0 ]; then
  echo "==> Starting shell"
else
  echo "==> Running command"
fi

docker compose exec python /usr/local/bin/docker-entrypoint.sh "$@"
