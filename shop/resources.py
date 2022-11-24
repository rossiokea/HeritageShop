from import_export import resources
from shop.models import Vehicle, Trailer, Equipment


class VehicleResource(resources.ModelResource):
    class Meta:
        import_id_fields = ['vehicle_id']
        model = Vehicle


class TrailerResource(resources.ModelResource):
    class Meta:
        import_id_fields = ['trailer_id']
        model = Trailer


class EquipmentResource(resources.ModelResource):
    class Meta:
        import_id_fields = ['equipment_id']
        model = Equipment
