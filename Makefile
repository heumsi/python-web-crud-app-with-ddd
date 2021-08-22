test-unit:
	pytest tests/unit

test-integration:
	#docker compose up --build
	pytest tests/integration
	#docker compose down -v

test-e2e:
	docker compose up --build
	pytest tests/e2e
	docker compose down -v

build:
	poetry export -o requirements.txt --without-hashes
	docker build -t python-web-crud-app-with-ddd .

run:
	python app/main.py