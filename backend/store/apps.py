from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store"
    
    def ready(self):
        """
        Overrides the ready method to connect signals when the app is ready.

        This method ensures that the signals defined in the store app's signals.py 
        are imported and connected when the app starts. This allows pre_save and 
        post_delete signals to handle product image deletion logic.
        
        Importing the signals here guarantees that they are registered when 
        Django starts the application.
        """
        import store.signals  # Import the signals module
        import store.logging_signals 