# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

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
