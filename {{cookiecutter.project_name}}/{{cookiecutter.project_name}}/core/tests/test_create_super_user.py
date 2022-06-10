import pytest
from django.contrib.auth import authenticate
from django.core import management

from {{cookiecutter.project_name}}.core.management.commands.create_super_user import create_super_user


@pytest.fixture
def super_user():
    create_super_user("username", "password")


@pytest.mark.django_db
def test_create_super_user_works(super_user):
    super_user = authenticate(username="username", password="password")  # nosec

    assert super_user is not None
    assert super_user.is_superuser


@pytest.mark.django_db
def test_does_create_super_user_works_from_cli(super_user):
    management.call_command(  # nosec
        "create_super_user",
        username="username",
        password="password",
    )
    super_user = authenticate(username="username", password="password")  # nosec

    assert super_user is not None
    assert super_user.is_superuser


@pytest.mark.django_db
def test_updates_password_if_user_exists(super_user):
    create_super_user("username", "new_password")
    super_user = authenticate(username="username", password="new_password")  # nosec
    assert super_user is not None
