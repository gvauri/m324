.PHONY: docker docker-run

docker:
	docker build -t sinus:latest .

docker-run: docker
    docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -u "$(id -u)":"$(id -g)" sinus:latest