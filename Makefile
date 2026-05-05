.PHONY: build test clean run

build:
	@echo "Building net-parser..."
	go build -o bin/net-parser ./cmd/...

test:
	go test ./... -v -cover

clean:
	rm -rf bin/ dist/

run: build
	./bin/net-parser
