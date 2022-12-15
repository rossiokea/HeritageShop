from datetime import date
from django import forms
from shop.models import *

department_choices = (('', 'Select One'),
                      ('10', 'Construction'),
                      ('20', 'Maintenance'),
                      ('50', 'Admin'))


class CreateVehicleForm(forms.ModelForm):
    vehicle_department = forms.MultipleChoiceField

    def __init__(self, *args, **kwargs):
        super(CreateVehicleForm, self).__init__(*args, **kwargs)

        self.fields['vehicle_license'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_license'].label = 'License#'
        self.fields['vehicle_license'].widget.attrs['style'] = 'width:10ch'
        self.fields['vehicle_license'].widget.attrs['placeholder'] = 'License'

        self.fields['vehicle_vin'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_vin'].label = 'Vin#'
        self.fields['vehicle_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['vehicle_vin'].widget.attrs['placeholder'] = 'Vehicle VIN'

        self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_identifier'].label = 'Heritage Equip#'
        self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['vehicle_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['vehicle_department'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_department'].label = 'Heritage Dept#'
        self.fields['vehicle_department'].widget.attrs['style'] = 'width:20ch'

        self.fields['vehicle_short_name'].label = 'Short Name'
        self.fields['vehicle_short_name'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_short_name'].widget.attrs['style'] = 'width:30ch'

        self.fields['vehicle_description'].label = 'Description'
        self.fields['vehicle_description'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_description'].widget.attrs['style'] = 'width:60ch'

        self.fields['service_period'].label = 'Service Period (mos.)'
        self.fields['service_period'].widget.attrs['class'] = 'form-control'
        self.fields['service_period'].widget.attrs['style'] = 'width:10ch'
        self.fields['service_period'].widget.attrs['value'] = 6

        self.fields['service_period_miles'].label = 'Service Period (mi.)'
        self.fields['service_period_miles'].widget.attrs['class'] = 'form-control'
        self.fields['service_period_miles'].widget.attrs['style'] = 'width:10ch'
        self.fields['service_period_miles'].widget.attrs['value'] = 5000

    class Meta:
        model = Vehicle
        fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
                  'vehicle_department', 'vehicle_short_name', 'vehicle_description', 'service_period', 'service_period_miles']

        widgets = {'vehicle_department': forms.Select(choices=department_choices)}


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateVehicleForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm1, self).__init__(*args, **kwargs)

        self.fields['vehicle_license'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_license'].label = 'License#'
        self.fields['vehicle_license'].widget.attrs['style'] = 'width:12ch'
        self.fields['vehicle_license'].widget.attrs['placeholder'] = 'License'

        self.fields['vehicle_vin'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_vin'].label = 'Vin#'
        self.fields['vehicle_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['vehicle_vin'].widget.attrs['placeholder'] = 'Vehicle VIN'

        self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_identifier'].label = 'Heritage Equip#'
        self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['vehicle_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['vehicle_short_name'].label = 'Short Name'
        self.fields['vehicle_short_name'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_short_name'].widget.attrs['style'] = 'width:30ch'

        self.fields['vehicle_description'].label = 'Description'
        self.fields['vehicle_description'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_description'].widget.attrs['style'] = 'width:60ch'

        self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_identifier'].label = 'Heritage Equip#'
        self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['vehicle_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['vehicle_department'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_department'].label = 'Heritage Dept:'
        self.fields['vehicle_department'].widget.attrs['style'] = 'width:20ch'

        self.fields['assigned_employee'].widget.attrs['class'] = 'form-control'
        self.fields['assigned_employee'].label = 'Assigned Employee'
        self.fields['assigned_employee'].widget.attrs['style'] = 'width:50ch'

        self.fields['assigned_trailer'].widget.attrs['class'] = 'form-control'
        self.fields['assigned_trailer'].label = 'Assigned Trailer'
        self.fields['assigned_trailer'].widget.attrs['style'] = 'width:40ch'

        self.fields['track_weekly_miles'].label = 'Weekly Miles Ck'
        self.fields['track_weekly_miles'].widget.attrs['class'] = 'form-control'
        self.fields['track_weekly_miles'].widget.attrs['style'] = 'width:15ch'

        self.fields['vehicle_status'].label = 'Status'
        self.fields['vehicle_status'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_status'].widget.attrs['style'] = 'width:15ch'




    class Meta:
        model = Vehicle
        fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
                  'vehicle_short_name', 'vehicle_description', 'vehicle_department',
                  'assigned_employee', 'assigned_trailer', 'track_weekly_miles', 'vehicle_status']


class UpdateVehicleForm2(forms.ModelForm):
    vehicle_department = forms.MultipleChoiceField

    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm2, self).__init__(*args, **kwargs)

        self.fields['vehicle_identifier'].disabled = True
        self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_identifier'].label = 'Heritage Equip#'
        self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['vehicle_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['service_period'].label = 'Service Period (mos.)'
        self.fields['service_period'].widget.attrs['class'] = 'form-control'
        self.fields['service_period'].widget.attrs['style'] = 'width:10ch'

        self.fields['service_period_miles'].label = 'Service Period (mi.)'
        self.fields['service_period_miles'].widget.attrs['class'] = 'form-control'
        self.fields['service_period_miles'].widget.attrs['style'] = 'width:10ch'

        self.fields['last_service'].label = 'Last Service Date'
        self.fields['last_service'].widget.attrs['class'] = 'form-control'
        self.fields['last_service'].widget.attrs['style'] = 'width:16ch'

        self.fields['last_service_miles'].label = 'Last Service Miles'
        self.fields['last_service_miles'].widget.attrs['class'] = 'form-control'
        self.fields['last_service_miles'].widget.attrs['style'] = 'width:16ch'

        self.fields['weekly_miles'].label = 'Weekly Miles'
        self.fields['weekly_miles'].widget.attrs['class'] = 'form-control'
        self.fields['weekly_miles'].widget.attrs['style'] = 'width:16ch'

        self.fields['next_service'].label = 'Next Service Date'
        self.fields['next_service'].widget.attrs['class'] = 'form-control'
        self.fields['next_service'].widget.attrs['style'] = 'width:16ch'

        self.fields['next_service_miles'].label = 'Next Service Miles'
        self.fields['next_service_miles'].widget.attrs['class'] = 'form-control'
        self.fields['next_service_miles'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = Vehicle
        fields = ['vehicle_identifier', 'service_period','service_period_miles', 'last_service', 'last_service_miles', 'weekly_miles',
                  'next_service',
                  'next_service_miles']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']

        widgets = {'last_service': DateInput(),
                   'next_service': DateInput(),
                   }


# This Has been depricated as fields have been moved to UpdateVehicleForm1
# class UpdateVehicleForm3(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(UpdateVehicleForm3, self).__init__(*args, **kwargs)
#         self.fields['vehicle_identifier'].disabled = True
#
#         self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-control'
#         self.fields['vehicle_identifier'].label = 'Heritage Equip#'
#         self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:15ch'
#         self.fields['vehicle_identifier'].widget.attrs['placeholder'] = 'XXX'
#
#         self.fields['vehicle_department'].widget.attrs['class'] = 'form-control'
#         self.fields['vehicle_department'].label = 'Heritage Dept:'
#         self.fields['vehicle_department'].widget.attrs['style'] = 'width:20ch'
#
#         self.fields['assigned_employee'].widget.attrs['class'] = 'form-control'
#         self.fields['assigned_employee'].label = 'Assigned Employee'
#         self.fields['assigned_employee'].widget.attrs['style'] = 'width:50ch'
#
#         self.fields['assigned_trailer'].widget.attrs['class'] = 'form-control'
#         self.fields['assigned_trailer'].label = 'Assigned Trailer'
#         self.fields['assigned_trailer'].widget.attrs['style'] = 'width:40ch'
#
#     class Meta:
#         model = Vehicle
#         fields = ['vehicle_identifier', 'vehicle_department', 'assigned_employee', 'assigned_trailer']
#         # fields = ['service_period', 'last_service', 'last_service_miles',
#         #        'next_service']
#         widgets = {'vehicle_department': forms.Select(choices=department_choices), }


class UpdateVehicleForm2Weekly(forms.ModelForm):
    # last_weekly_check = forms.DateField(widget=DateInput(), initial=date.today())

    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm2Weekly, self).__init__(*args, **kwargs)
        # self.fields['last_weekly_check'].initial = date.today()

        self.fields['vehicle_identifier'].disabled = True
        self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_identifier'].label = 'Heritage Equip#'
        self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['vehicle_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['last_service_miles'].label = 'Last Service Miles'
        self.fields['last_service_miles'].widget.attrs['class'] = 'form-control'
        self.fields['last_service_miles'].widget.attrs['style'] = 'width:16ch'

        # self.fields['last_weekly_check'].label = 'Last Mileage Check'
        # self.fields['last_weekly_check'].widget.attrs['class'] = 'form-control'
        # self.fields['last_weekly_check'].widget.attrs['style'] = 'width:16ch'
        # self.fields['last_weekly_check'].widget.attrs['value'] = date.today()

        self.fields['weekly_miles'].label = 'Weekly Miles'
        self.fields['weekly_miles'].widget.attrs['class'] = 'form-control'
        self.fields['weekly_miles'].widget.attrs['style'] = 'width:16ch'

        self.fields['next_service_miles'].label = 'Next Service Miles'
        self.fields['next_service_miles'].widget.attrs['class'] = 'form-control'
        self.fields['next_service_miles'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = Vehicle
        fields = ['vehicle_identifier', 'last_service_miles',  'weekly_miles', 'next_service_miles']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']
        widgets = {'last_weekly_check': DateInput()}


class UpdateVehicleForm4(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UpdateVehicleForm4, self).__init__(*args, **kwargs)

        self.fields['vehicle_identifier'].label = 'Heritage Equip#'
        self.fields['vehicle_identifier'].disabled = True
        self.fields['vehicle_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['vehicle_identifier'].widget.attrs['style'] = 'width:12ch'

        self.fields['last_dot'].label = 'Last DOT Inspection'
        self.fields['last_dot'].widget.attrs['class'] = 'form-control'
        self.fields['last_dot'].widget.attrs['style'] = 'width:16ch'

        self.fields['next_dot'].label = 'Next DOT Inspection'
        self.fields['next_dot'].widget.attrs['class'] = 'form-control'
        self.fields['next_dot'].widget.attrs['style'] = 'width:16ch'

        self.fields['last_dot_status'].label = 'Last DOT Inspection Status'
        self.fields['last_dot_status'].widget.attrs['class'] = 'form-control'
        self.fields['last_dot_status'].widget.attrs['style'] = 'width:12ch'

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

        self.fields['service_date'].label = 'Vehicle Service Date'
        self.fields['service_date'].widget.attrs['class'] = 'form-control'
        self.fields['service_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['service_notes'].label = 'Vehicle Service Notes'
        self.fields['service_notes'].widget.attrs['class'] = 'form-control'
        self.fields['service_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['service_miles'].label = 'Vehicle Service Miles'
        self.fields['service_miles'].widget.attrs['class'] = 'form-control'
        self.fields['service_miles'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = VehicleServiceRecord
        fields = ['service_date', 'service_miles', 'service_notes']
        widgets = {'service_date': DateInput()}


class ServiceRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceRecordUpdateForm, self).__init__(*args, **kwargs)

        self.fields['service_date'].label = 'Vehicle Service Date'
        self.fields['service_date'].widget.attrs['class'] = 'form-control'
        self.fields['service_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['service_notes'].label = 'Vehicle Service Notes'
        self.fields['service_notes'].widget.attrs['class'] = 'form-control'
        self.fields['service_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['service_miles'].label = 'Vehicle Service Miles'
        self.fields['service_miles'].widget.attrs['class'] = 'form-control'
        self.fields['service_miles'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = VehicleServiceRecord
        fields = ['service_date', 'service_miles', 'service_notes']
        widgets = {'service_date': DateInput()}


class RepairRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairRecordCreateForm, self).__init__(*args, **kwargs)

        self.fields['repair_date'].label = 'Vehicle Repair Date'
        self.fields['repair_date'].widget.attrs['class'] = 'form-control'
        self.fields['repair_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['repair_notes'].label = 'Vehicle Repair Notes'
        self.fields['repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['repair_miles'].label = 'Vehicle Repair Miles'
        self.fields['repair_miles'].widget.attrs['class'] = 'form-control'
        self.fields['repair_miles'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = VehicleRepairRecord
        fields = ['repair_date', 'repair_miles', 'repair_notes']
        widgets = {'repair_date': DateInput()}


class RepairRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RepairRecordUpdateForm, self).__init__(*args, **kwargs)

        self.fields['repair_date'].label = 'Vehicle Repair Date'
        self.fields['repair_date'].widget.attrs['class'] = 'form-control'
        self.fields['repair_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['repair_notes'].label = 'Vehicle Repair Notes'
        self.fields['repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['repair_miles'].label = 'Vehicle Repair Miles'
        self.fields['repair_miles'].widget.attrs['class'] = 'form-control'
        self.fields['repair_miles'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = VehicleRepairRecord
        fields = ['repair_date', 'repair_miles', 'repair_notes']
        widgets = {'repair_date': DateInput()}


class DotRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DotRecordCreateForm, self).__init__(*args, **kwargs)

        self.fields['dot_inspection_date'].label = 'Vehicle DOT Date'
        self.fields['dot_inspection_date'].widget.attrs['class'] = 'form-control'
        self.fields['dot_inspection_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['dot_repair_notes'].label = 'Vehicle DOT Notes'
        self.fields['dot_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['dot_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['dot_miles'].label = 'Vehicle DOT Miles'
        self.fields['dot_miles'].widget.attrs['class'] = 'form-control'
        self.fields['dot_miles'].widget.attrs['style'] = 'width:16ch'

        self.fields['dot_passed_inspection'].label = 'Vehicle DOT Status'
        self.fields['dot_passed_inspection'].widget.attrs['class'] = 'form-control'
        self.fields['dot_passed_inspection'].widget.attrs['style'] = 'width:12ch'

    class Meta:
        model = VehicleDotRecord
        fields = ['dot_inspection_date', 'dot_miles', 'dot_repair_notes', 'dot_passed_inspection']
        widgets = {'dot_inspection_date': DateInput()}


class DotRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DotRecordUpdateForm, self).__init__(*args, **kwargs)

        self.fields['dot_inspection_date'].label = 'Vehicle DOT Date'
        self.fields['dot_inspection_date'].widget.attrs['class'] = 'form-control'
        self.fields['dot_inspection_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['dot_repair_notes'].label = 'Vehicle DOT Notes'
        self.fields['dot_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['dot_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['dot_miles'].label = 'Vehicle DOT Miles'
        self.fields['dot_miles'].widget.attrs['class'] = 'form-control'
        self.fields['dot_miles'].widget.attrs['style'] = 'width:16ch'

        self.fields['dot_passed_inspection'].label = 'Vehicle DOT Status'
        self.fields['dot_passed_inspection'].widget.attrs['class'] = 'form-control'
        self.fields['dot_passed_inspection'].widget.attrs['style'] = 'width:12ch'

    class Meta:
        model = VehicleDotRecord
        fields = ['dot_inspection_date', 'dot_miles', 'dot_repair_notes', 'dot_passed_inspection']
        widgets = {'dot_inspection_date': DateInput()}
