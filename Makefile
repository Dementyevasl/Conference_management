ifndef PORT
	PORT=8080
endif

build:
	docker build -t conf-tool-dev --build-arg PORT=$(PORT) .

run: build
	docker run -p $(PORT):$(PORT) -it --rm --name conf-tool-dev conf-tool-dev