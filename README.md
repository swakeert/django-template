# Django Template

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) template for starting my django projects.

## Usage

```bash
$ pip install cookiecutter

$ cookiecutter https://github.com/swakeert/django-template
project_human_name [My App]: Super Awesome App
project_description [My very awesome app.]: Super awesome app that is going to change the world
project_name [my_app]: super_app

$ tree super_app
super_app
├── Dockerfile
├── README.md
├── docker-compose.yml
├── manage.py
├── pytest.ini
├── requirements
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
└── super_app
    ├── core
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── management
    │   │   ├── __init__.py
    │   │   └── commands
    │   │       ├── __init__.py
    │   │       └── create_super_user.py
    │   └── tests
    │       ├── __init__.py
    │       └── test_create_super_user.py
    └── super_app
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

7 directories, 20 files
```

## Contributing

Feel free to open PRs to make any improvements or something from the planned improvements.
If you find any problems, you can also raise an issue.

## Planned improvements

* CI/ CD entrypoint script
* Improve README
* Implement general auth endpoints like register, login, forgot password, token management, etc.

## Similar projects

For a much advanced version of this project, try out [cookiecutter-django](https://github.com/cookiecutter/cookiecutter-django).
