from django import forms
from shop.models import *


class CreateVehicleForm(forms.ModelForm):
    vehicle_department = forms.MultipleChoiceField

    def __init__(self, *args, **kwargs):
        super(CreateVehicleForm, self).__init__(*args, **kwargs)

        self.fields['vehicle_license'].widget.attrs['class'] = 'form-group'
        self.fields['vehicle_license'].label = 'License#'
        self.fields['vehicle_license'].widget.attrs['style'] = 'width:10ch'
        self.fields['vehicle_license'].widget.attrs['placeholder'] = 'License'

        self.fields['vehicle_vin'].widget.attrs['class'] = 'form-group'
        self.fields['vehicle_vin'].label = 'Vin#'
        self.fields['vehicle_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['vehicle_vin'].widget.attrs['placeholder'] = 'Vehicle VIN'

        self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-group'
        self.fields['vehicle_identifier'].label = 'Heritage Equip#'
        self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['vehicle_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['vehicle_department'].widget.attrs['class'] = 'form-group'
        self.fields['vehicle_department'].label = 'Heritage Dept#'
        self.fields['vehicle_department'].widget.attrs['style'] = 'width:20ch'

    class Meta:
        department_choices = (('', 'Select One'),
                              ('10', 'Construction'),
                              ('20', 'Maintenance'),
                              ('50', 'Admin'))
        model = Vehicle
        fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
                  'vehicle_department', 'vehicle_short_name', 'vehicle_description']

        widgets = {'vehicle_department': forms.Select(choices=department_choices)}


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateVehicleForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm1, self).__init__(*args, **kwargs)

    class Meta:
        model = Vehicle
        fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
                  'vehicle_short_name', 'vehicle_description', 'vehicle_status']


class UpdateVehicleForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm2, self).__init__(*args, **kwargs)
        self.fields['vehicle_identifier'].disabled = True

    class Meta:
        model = Vehicle
        fields = ['vehicle_identifier', 'service_period', 'last_service', 'last_service_miles', 'next_service']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']

        widgets = {'last_service': DateInput(),
                   'next_service': DateInput(),
                   }


class UpdateVehicleForm3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm3, self).__init__(*args, **kwargs)
        self.fields['vehicle_identifier'].disabled = True

    class Meta:
        model = Vehicle
        fields = ['vehicle_identifier', 'vehicle_department', 'assigned_employee', 'assigned_trailer']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']


class UpdateVehicleForm4(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm4, self).__init__(*args, **kwargs)
        self.fields['vehicle_identifier'].disabled = True

    class Meta:
        model = Vehicle
        fields = ['vehicle_identifier', 'last_dot', 'next_dot', 'last_dot_status']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']
        widgets = {'last_dot': DateInput(),
                   'next_dot': DateInput(),
                   }


class ServiceRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VehicleServiceRecord
        fields = ['service_date', 'service_miles', 'service_notes']
        widgets = {'service_date': DateInput()}


class ServiceRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VehicleServiceRecord
        fields = ['service_date', 'service_miles', 'service_notes']
        widgets = {'service_date': DateInput()}


class RepairRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VehicleRepairRecord
        fields = ['repair_date', 'repair_miles', 'repair_notes']
        widgets = {'repair_date': DateInput()}


class RepairRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VehicleRepairRecord
        fields = ['repair_date', 'repair_miles', 'repair_notes']
        widgets = {'service_date': DateInput()}


class DotRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DotRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VehicleDotRecord
        fields = ['dot_inspection_date', 'dot_miles', 'dot_repair_notes', 'dot_passed_inspection']
        widgets = {'dot_inspection_date': DateInput()}


class DotRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DotRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = VehicleDotRecord
        fields = ['dot_inspection_date', 'dot_miles', 'dot_repair_notes', 'dot_passed_inspection']
        widgets = {'service_date': DateInput()}

    '''
    dot_inspection_date = models.DateField()
    repair_miles = models.IntegerField(blank=True, null=True)
    dot_repair_notes = models.TextField()
    dot_passed_inspection = models.BooleanField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    '''
    #
    # class NoValidationUserProfileForm(CreateServiceRecordForm):
    #     def __init__(self, *args, **kwargs):
    #         super(NoValidationUserProfileForm, self).__init__(*args, **kwargs)
    #         self.fields['service_date'].required = False
    #         self.fields['service_miles'].required = False
    #         self.fields['service_date'].required = False
    #
    #     class Meta:
    #         model = VehicleServiceRecord
    #         fields = ['service_date', 'service_miles', 'service_notes']
    #         widgets = {'service_date': DateInput()}

    '''
        vehicle_license = forms.CharField()
        vehicle_vin = forms.CharField(max_length=17)
        vehicle_identifier = forms.CharField(max_length=15)
        vehicle_department = forms.IntegerField()
        vehicle_short_name = forms.CharField(max_length=20)
        vehicle_description = forms.CharField(max_length=50)
    
    '''

    '''
        vehicle_id = models.AutoField(primary_key=True, editable=False)
        vehicle_license = models.CharField(max_length=7)
        vehicle_vin = models.CharField(max_length=17)
        vehicle_identifier = models.CharField(max_length=15)
        vehicle_department = models.IntegerField(blank=True, null=True)
        vehicle_short_name = models.CharField(max_length=20, blank=True, null=True)
        vehicle_description = models.CharField(max_length=50, blank=True, null=True)
    
    '''
