
.DEFAULT_GOAL := help


check-%:
	@: $(if $(value $*),,$(error $* is undefined))


help:
	@echo "Targets:"
	@echo ""
	@grep -E '^([a-zA-Z_-])+%*:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-40s\033[0m %s\n", $$1, $$2}'


format-%:
	(cd $* && poetry run format)


lint-%:
	(cd $* && poetry run lint)


.PHONY: format
format:| format-api format-package  ## run format


.PHONY: lint
lint:| format lint-api lint-package ## run lint


.PHONY: docker-compose_up
docker-compose_up:  ## run docker
	docker compose up --build -d


.PHONY: package
package: ## create package
	(cd package && poetry run build)


.PHONY: register_package
register_package:| check-VERSION ## register package
	(cd package && curl -X POST \
		'http://localhost:8080/api/v1/repo/package' \
		-H 'accept: application/json' \
		-H 'Content-Type: multipart/form-data' \
		-F 'f=@dist/fastpypi-package-${VERSION}.tar.gz;type=application/x-gzip')
