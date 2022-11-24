from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from shop.resources import VehicleResource, TrailerResource, EquipmentResource

from shop.models import Vehicle, \
    VehicleServiceRecord, VehicleRepairRecord, VehicleDotRecord, \
    Trailer, \
    TrailerServiceRecord, TrailerRepairRecord, TrailerDotRecord, \
    Equipment, \
    EquipmentServiceRecord, EquipmentRepairRecord


@admin.register(Vehicle)
class VehicleImportExport(ImportExportModelAdmin):
    resource_class = VehicleResource


@admin.register(Trailer)
class TrailerImportExport(ImportExportModelAdmin):
    resource_class = TrailerResource


@admin.register(Equipment)
class EquipmentImportExport(ImportExportModelAdmin):
    resource_class = EquipmentResource


# Register your models here.
# admin.site.register(Vehicle)
admin.site.register(VehicleServiceRecord)
admin.site.register(VehicleRepairRecord)
admin.site.register(VehicleDotRecord)

# admin.site.register(Trailer)
admin.site.register(TrailerServiceRecord)
admin.site.register(TrailerRepairRecord)
admin.site.register(TrailerDotRecord)

# admin.site.register(Equipment)
admin.site.register(EquipmentServiceRecord)
admin.site.register(EquipmentRepairRecord)
