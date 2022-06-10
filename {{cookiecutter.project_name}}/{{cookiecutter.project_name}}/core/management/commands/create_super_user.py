from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


def create_super_user(username, password):
    """
    Create a superuser. If username already exists, it updates the password to the given password
    """
    User = get_user_model()
    user, _ = User.objects.get_or_create(username=username)
    user.set_password(password)
    user.is_staff, user.is_superuser = True, True
    user.save()


class Command(BaseCommand):
    help = "Create a superuser through CLI. Only for local use. If username already exists, it updates the password to the given password"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            dest="username",
            help="Specifies the username for the superuser.",
        )

        parser.add_argument(
            "--password",
            dest="password",
            help="Specifies the password for the superuser.",
        )

    def handle(self, *args, username, password, **options):
        create_super_user(username, password)
