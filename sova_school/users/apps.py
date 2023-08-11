from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "sova_school.users"

    def ready(self):
        import sova_school.users.signals
        result = super().ready()
        return result
