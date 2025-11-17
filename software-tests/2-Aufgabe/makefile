start_mongodb:
    docker run --name test-db -d -p 27017:27017 mongo

test:
	python -m coverage run ./test_file.py;

coverage:test-with-coverage
	python -m coverage report

clean_coverage:
	rm .coverage

clean_mongodb:
    docker stop test-db
    docker rm test-db

 test-with-coverage: test coverage clean_coverage

 start_integrations_test:start_mongodb test_with_coverage clean_mongodb
