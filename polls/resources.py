from import_export import resources
from .models import Equipment

class PersonResource(resources.ModelResource):
    class Meta:
        model = Equipment
        skip_unchanged = True
        use_bulk = True