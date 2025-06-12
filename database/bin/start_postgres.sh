#!/bin/bash
export DOCKER_DEFAULT_PLATFORM=linux/amd64
docker compose -f "$(dirname "$0")/../docker-compose.yml" up -d