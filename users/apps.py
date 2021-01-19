from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # To run signals as per the django documentation
    def ready(self):
        import users.signals
