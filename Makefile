build:
	poetry install
	poetry run pytest
	poetry run black .
	poetry run isort -rc .
	poetry run flake8
	poetry build

autoformat:
	poetry run black .
	poetry run isort -rc .

test:
	poetry run pytest
	$(MAKE) autoformat
	poetry run flake8
