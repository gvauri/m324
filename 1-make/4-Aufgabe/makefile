IMAGE_NAME=cpp-container

.PHONY: compile docker-build docker-run clean

compile:
	@if [ -f main.cpp ]; then \
		g++ main.cpp -o a.out; \
	fi
run: compile
	@if [ -f main ]; then \
		./main; \
	fi
docker-build:
	docker build -t $(IMAGE_NAME) .

docker-run: docker-build
	docker run  --rm $(IMAGE_NAME)

clean:
	docker rmi -f $(IMAGE_NAME)