export REGISTRY_NAME?=ghcr.io/arctaruslimited
export VERSION=1.0.0

build:
	docker build --label version=$(VERSION) -t $(REGISTRY_NAME)/catalysis:$(VERSION) .

push: build
	docker push $(REGISTRY_NAME)/catalysis:$(VERSION)
