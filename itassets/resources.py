from import_export import resources
from .models import It_Prodcuts

class It_ProdcutsResources(resources.ModelResource):
    class Meta:
        model = It_Prodcuts
        skip_unchanged = True
        use_bulk = True