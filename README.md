# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Docker

This project uses docker to build and run locally.

```bash
# To build and run the container.
$ docker-compose build
$ docker-compose up

# Or do it in one command.
$ docker-compose up -b

# Run a custom command inside the container.
$ docker-compose run --rm {{cookiecutter.project_name}}_backend <command>

# For example:
$ docker-compose run --rm {{cookiecutter.project_name}}_backend python manage.py makemigrations
```

## Pre-commit

This repo uses [Pre-commit hooks](https://pre-commit.com/#install) to ensure code quality.

## Linting

This repo follow [Black](https://github.com/psf/black) linting standards, with additional import sorting using isort and flake8.

## Testing: Pytest

This repo uses pytest for testing.

```bash
docker-compose run --rm {{cookiecutter.project_name}}_backend pytest
```

## django-template

This project was initialised using [this template](https://github.com/swakeert/django-template)
