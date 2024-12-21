from django.apps import AppConfig



class ProfileeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.profilee'




class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'

    def ready(self):
        import profilee.signals
