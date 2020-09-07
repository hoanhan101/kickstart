COMPOSE_FILE := local.yml

.PHONY: deploy docker lint migrate test help
.DEFAULT_GOAL := help

deploy: docker  ## Run a local development deployment
	docker-compose -f ${COMPOSE_FILE} up

docker:  ## Build a local docker image
	docker-compose -f ${COMPOSE_FILE} build

lint:  ## Run linting
	flake8

migrate: docker  ## Run migration
	docker-compose -f ${COMPOSE_FILE} run --rm django python manage.py migrate

test: docker  ## Run unit tests and produce coverage report
	docker-compose -f local.yml run --rm django coverage run -m pytest
	docker-compose -f local.yml run --rm django coverage report

help:  ## Print usage information
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
