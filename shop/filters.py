import django_filters


class VehicleFilter(django_filters.filterset):
    class Meta:
        model = Vehicle
        fields = ['vehicle_']
