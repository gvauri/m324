start_mongodb:
	 docker run --name test_db -d -p 27017:27017 mongo

test:
	python -m coverage run ./test_db.py

coverage:
	python -m coverage report

clean_coverage:
	rm .coverage

clean_mongodb:
	docker stop test_db
	docker rm test_db

test_with_coverage: test coverage clean_coverage

start_integrations_test: start_mongodb test_with_coverage clean_mongodb
