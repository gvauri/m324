.PHONY: linting

coverage: src/house_exception.py src/house.py tests/test.py
	python3 -m coverage run -m unittest discover tests
	python3 -m coverage report
	python3 -m coverage xml -i

	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	rm -f .coverage

linting: coverage
	docker run --rm \
		--platform linux/amd64 \
		-e SONAR_HOST_URL="http://sonarqube:9000" \
		-e SONAR_SCANNER_OPTS="-Dsonar.projectKey=house" \
		-e SONAR_TOKEN="squ_4c3e0e79db399d6991ea270105de0ba796e2054c" \
		--network sonar-net \
		-v $(shell pwd):/usr/src \
		sonarsource/sonar-scanner-cli

	rm -f coverage.xml
