.PHONY: linting

linting: coverage.xml
	 docker run --rm \
    --platform linux/amd64 \
    -e SONAR_HOST_URL="http://sonarqube:9000" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=house" \
    -e SONAR_TOKEN="sqa_5201cc3bc3873a377045c3d0b5ddf8be9fbfc8c1" \
    --network sonar-net \
    -v "$(pwd)":/usr/src \
    sonarsource/sonar-scanner-cli

	rm -f coverage.xml

coverage.xml: src/house.py tests/test.py
	python3 -m coverage run -m unittest discover tests
	python3 -m coverage report
	python3 -m coverage xml -i

	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	rm -f .coverage