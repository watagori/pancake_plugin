# pancake_plugin

## docker

### for start

$ docker-compose up -d

### for access to shell in the container

$ docker-compose exec pancake_plugin bash

### for end

$ docker-compose down

### for remove

$ docker-compose down --rmi all --volumes --remove-orphans

### pytest

$ pytest --cov=src --cov-branch --cov-report=term-missing -vv
