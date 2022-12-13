import uuid

from django.db import models

IS_ACTIVE = [(True, 'Active'), (False, 'Inactive')]
DOT_STATUS = [(True, 'Passed'), (False, 'Failed')]
ASSIGNED_DEPARTMENT = [('', 'Select One'),
                       (10, 'Construction'),
                       (20, 'Maintenance'),
                       (50, 'Admin')]
TRACK_WEEKLY = [(True, 'Yes'), (False, 'No')]

# Create your models here.
class Trailer(models.Model):
    trailer_id = models.AutoField(primary_key=True, editable=False)
    trailer_license = models.CharField(max_length=7)
    trailer_vin = models.CharField(max_length=17)
    trailer_identifier = models.IntegerField()
    trailer_department = models.IntegerField(choices=ASSIGNED_DEPARTMENT, blank=True, null=True)
    trailer_short_name = models.CharField(max_length=30, blank=True, null=True)
    trailer_description = models.CharField(max_length=60, blank=True, null=True)
    # Service Attributes
    trailer_service_period = models.IntegerField(blank=True, null=True)
    trailer_last_service = models.DateField(blank=True, null=True)
    trailer_next_service = models.DateField(blank=True, null=True)
    # DOT Attributes
    trailer_last_dot = models.DateField(blank=True, null=True)
    trailer_next_dot = models.DateField(blank=True, null=True)
    trailer_last_dot_status = models.BooleanField(choices=DOT_STATUS, default=True, blank=True)
    # Trailer Status
    trailer_status = models.BooleanField(choices=IS_ACTIVE, default=True, blank=True)

    # Trailer Return String
    def __str__(self):
        return f"Trailer ID: {self.trailer_identifier} License: {self.trailer_license}"


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True, editable=False)
    vehicle_license = models.CharField(max_length=10)
    vehicle_vin = models.CharField(max_length=20)
    vehicle_identifier = models.IntegerField()
    vehicle_department = models.IntegerField(choices=ASSIGNED_DEPARTMENT, blank=True, null=True)
    vehicle_short_name = models.CharField(max_length=30, blank=True, null=True)
    vehicle_description = models.CharField(max_length=60, blank=True, null=True)
    vehicle_status = models.BooleanField(choices=IS_ACTIVE, default=True, blank=True)

    # End Required Fields
    # Assignements
    assigned_employee = models.CharField(max_length=50, blank=True, null=True)
    assigned_trailer = models.OneToOneField(Trailer, on_delete=models.CASCADE, blank=True, null=True)
    # Service Attributes
    service_period = models.IntegerField(blank=True, null=True)
    last_service = models.DateField(blank=True, null=True)
    last_service_miles = models.IntegerField(blank=True, null=True)
    next_service = models.DateField(blank=True, null=True)
    next_service_miles = models.IntegerField(blank=True, null=True)

    # Vehicles weekly mileage check
    track_weekly_miles = models.BooleanField(choices=TRACK_WEEKLY, default=False, blank=False)
    weekly_miles = models.IntegerField(blank=True, null=True)
    last_weekly_check = models.DateField(blank=True, null=True)

    # DOT Attributes
    last_dot = models.DateField(blank=True, null=True)
    next_dot = models.DateField(blank=True, null=True)
    last_dot_status = models.BooleanField(choices=DOT_STATUS, default=True, blank=True)

    def __str__(self):
        return f"Vehicle ID: {self.vehicle_identifier} License: {self.vehicle_license}"


class VehicleServiceRecord(models.Model):
    # vehicle_id = models.IntegerField()
    service_date = models.DateField(blank=True, null=True)
    service_miles = models.IntegerField(blank=True, null=True)
    service_notes = models.TextField(max_length=250, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class VehicleRepairRecord(models.Model):
    # vehicle_id = models.IntegerField()
    repair_date = models.DateField(blank=True, null=True)
    repair_miles = models.IntegerField(blank=True, null=True)
    repair_notes = models.TextField(max_length=250, blank=True, null=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class VehicleDotRecord(models.Model):
    # vehicle_id = models.IntegerField()
    dot_inspection_date = models.DateField()
    dot_miles = models.IntegerField(blank=True, null=True)
    dot_repair_notes = models.TextField(max_length=250, blank=True, null=True)
    dot_passed_inspection = models.BooleanField(choices=DOT_STATUS, default=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


# class Trailer(models.Model):
#     trailer_id = models.AutoField(primary_key=True, editable=False)
#     trailer_license = models.CharField(max_length=7)
#     trailer_vin = models.CharField(max_length=17)
#     vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
#     service_period = models.IntegerField()
#     last_service = models.DateField()
#     next_service = models.DateField()


class TrailerServiceRecord(models.Model):
    trailer_service_date = models.DateField(blank=True, null=True)
    trailer_service_notes = models.TextField(max_length=250, blank=True, null=True)
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)


class TrailerRepairRecord(models.Model):
    trailer_repair_date = models.DateField(blank=True, null=True)
    trailer_repair_notes = models.TextField(max_length=250, blank=True, null=True)
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)


class TrailerDotRecord(models.Model):
    trailer_dot_inspection_date = models.DateField(blank=True, null=True)
    trailer_dot_repair_notes = models.TextField(blank=True, null=True)
    trailer_dot_passed_inspection = models.BooleanField(choices=DOT_STATUS, default=True)
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)


# ***********  START EQUIPMENT MODELS *************************

#
# class Equipment(models.Model):
#     equipment_id = models.IntegerField()
#     equipment_vin = models.CharField(max_length=17)
#     equipment_service_period = models.IntegerField()
#
#     equipment_last_service = models.DateField()
#     equipment_next_service = models.DateField()


class Equipment(models.Model):
    equipment_id = models.AutoField(primary_key=True, editable=False, blank=True)
    equipment_vin = models.CharField(max_length=17, blank=True, null=True)
    equipment_identifier = models.IntegerField()
    equipment_department = models.IntegerField(choices=ASSIGNED_DEPARTMENT, blank=True, null=True)
    equipment_short_name = models.CharField(max_length=30, blank=True, null=True)
    equipment_description = models.CharField(max_length=60, blank=True, null=True)
    # End Required Fields

    # Assignements

    equipment_assigned_employee = models.CharField(max_length=50, blank=True, null=True)
    equipment_assigned_project = models.CharField(max_length=75, blank=True, null=True)
    equipment_assigned_date = models.DateField(blank=True, null=True)

    # Service Attributes
    equipment_service_period = models.IntegerField(blank=True, null=True)
    equipment_last_service = models.DateField(blank=True, null=True)
    equipment_last_service_hours = models.IntegerField(blank=True, null=True)
    equipment_next_service = models.DateField(blank=True, null=True)
    equipment_next_service_hours = models.IntegerField(blank=True, null=True)

    # DOT Attributes
    equipment_last_dot = models.DateField(blank=True, null=True)
    equipment_next_dot = models.DateField(blank=True, null=True)
    equipment_last_dot_status = models.BooleanField(default=True, blank=True)

    # Trailer Status
    equipment_status = models.BooleanField(choices=IS_ACTIVE, default=True, blank=True)

    def __str__(self):
        return f"Equipment ID: {self.equipment_identifier} VIN: {self.equipment_vin}"


class EquipmentServiceRecord(models.Model):
    # vehicle_id = models.IntegerField()
    equipment_service_date = models.DateField(blank=True, null=True)
    equipment_service_hours = models.IntegerField(blank=True, null=True)
    equipment_next_service_hours = models.IntegerField(blank=True, null=True)
    equipment_service_notes = models.TextField(max_length=250, blank=True, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)


class EquipmentRepairRecord(models.Model):
    # vehicle_id = models.IntegerField()
    equipment_repair_date = models.DateField(blank=True, null=True)
    equipment_repair_miles = models.IntegerField(blank=True, null=True)
    equipment_repair_notes = models.TextField(max_length=250, blank=True, null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)


class Tools(models.Model):
    pass
