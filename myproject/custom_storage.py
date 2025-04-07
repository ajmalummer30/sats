from django.core.files.storage import Storage
import os

class SharedDriveStorage(Storage):
    def __init__(self, location=None):
        if location is None:
            # Provide a default location if none is provided
            location = '\\\\192.168.1.110\\test\\'
        self.location = location

    def _open(self, name, mode='rb'):
        return open(os.path.join(self.location, name), mode)

    def _save(self, name, content):
        with open(os.path.join(self.location, name), 'wb') as destination:
            for chunk in content.chunks():
                destination.write(chunk)
        return name

    def get_available_name(self, name, max_length=None):
        return name

    def url(self, name):
        # Return the URL to access the file
        return os.path.join(self.location, name).replace('\\', '/')