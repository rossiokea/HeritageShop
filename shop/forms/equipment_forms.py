from django import forms

from shop.models import Equipment, EquipmentServiceRecord, EquipmentRepairRecord, Trailer, TrailerServiceRecord, \
    TrailerDotRecord, TrailerRepairRecord

department_choices = (('', 'Select One'),
                      ('10', 'Construction'),
                      ('20', 'Maintenance'),
                      ('50', 'Admin'))


class CreateEquipmentForm(forms.ModelForm):
    equipment_department = forms.MultipleChoiceField

    def __init__(self, *args, **kwargs):
        super(CreateEquipmentForm, self).__init__(*args, **kwargs)

        self.fields['equipment_vin'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_vin'].label = 'Vin#'
        self.fields['equipment_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['equipment_vin'].widget.attrs['placeholder'] = 'Equipment VIN'

        self.fields['equipment_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_identifier'].label = 'Heritage Equip#'
        self.fields['equipment_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['equipment_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['equipment_department'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_department'].label = 'Heritage Dept#'
        self.fields['equipment_department'].widget.attrs['style'] = 'width:20ch'

        self.fields['equipment_short_name'].label = 'Short Name'
        self.fields['equipment_short_name'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_short_name'].widget.attrs['style'] = 'width:30ch'

        self.fields['equipment_description'].label = 'Description'
        self.fields['equipment_description'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_description'].widget.attrs['style'] = 'width:60ch'

    class Meta:
        model = Equipment
        fields = ['equipment_vin', 'equipment_identifier',
                  'equipment_department', 'equipment_short_name', 'equipment_description']

        widgets = {'equipment_department': forms.Select(choices=department_choices)}


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateEquipmentForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateEquipmentForm1, self).__init__(*args, **kwargs)

        self.fields['equipment_vin'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_vin'].label = 'Vin#'
        self.fields['equipment_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['equipment_vin'].widget.attrs['placeholder'] = 'Equipment VIN'

        self.fields['equipment_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_identifier'].label = 'Heritage Equip#'
        self.fields['equipment_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['equipment_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['equipment_short_name'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_short_name'].label = 'Short Name'
        self.fields['equipment_short_name'].widget.attrs['style'] = 'width:30ch'

        self.fields['equipment_description'].label = 'Description'
        self.fields['equipment_description'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_description'].widget.attrs['style'] = 'width:60ch'

        self.fields['equipment_status'].label = 'Status'
        self.fields['equipment_status'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_status'].widget.attrs['style'] = 'width:15ch'

    class Meta:
        model = Equipment
        fields = ['equipment_vin', 'equipment_identifier',
                  'equipment_short_name', 'equipment_description', 'equipment_status']


class UpdateEquipmentForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateEquipmentForm2, self).__init__(*args, **kwargs)

        self.fields['equipment_identifier'].disabled = True
        self.fields['equipment_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_identifier'].label = 'Heritage Equip#'
        self.fields['equipment_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['equipment_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['equipment_service_period'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_service_period'].label = 'Equipment Service Period (Hrs)'
        self.fields['equipment_service_period'].widget.attrs['style'] = 'width:15ch'

        self.fields['equipment_last_service_hours'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_last_service_hours'].label = 'Last Service Hours'
        self.fields['equipment_last_service_hours'].widget.attrs['style'] = 'width:15ch'

        self.fields['equipment_next_service_hours'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_next_service_hours'].label = 'Next Service Hours'
        self.fields['equipment_next_service_hours'].widget.attrs['style'] = 'width:15ch'

        self.fields['equipment_last_service'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_last_service'].label = 'Last Service Date'
        self.fields['equipment_last_service'].widget.attrs['style'] = 'width:16ch'

        self.fields['equipment_next_service'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_next_service'].label = 'Next Service Date'
        self.fields['equipment_next_service'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = Equipment
        fields = ['equipment_identifier', 'equipment_service_period', 'equipment_last_service_hours',
                  'equipment_next_service_hours',
                  'equipment_last_service', 'equipment_next_service']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']
        widgets = {'equipment_last_service': DateInput(),
                   'equipment_next_service': DateInput(),
                   }


class UpdateEquipmentForm3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateEquipmentForm3, self).__init__(*args, **kwargs)

        self.fields['equipment_identifier'].disabled = True
        self.fields['equipment_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_identifier'].label = 'Heritage Equip#'
        self.fields['equipment_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['equipment_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['equipment_department'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_department'].label = 'Heritage Dept:'
        self.fields['equipment_department'].widget.attrs['style'] = 'width:20ch'

        self.fields['equipment_assigned_employee'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_assigned_employee'].label = 'Assigned Employee'
        self.fields['equipment_assigned_employee'].widget.attrs['style'] = 'width:50ch'

        self.fields['equipment_assigned_project'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_assigned_project'].label = 'Assigned Project'
        self.fields['equipment_assigned_project'].widget.attrs['style'] = 'width:75ch'

    class Meta:
        model = Equipment
        fields = ['equipment_identifier', 'equipment_department', 'equipment_assigned_employee',
                  'equipment_assigned_project']

        widgets = {'equipment_department': forms.Select(choices=department_choices)}


class ServiceRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceRecordCreateForm, self).__init__(*args, **kwargs)

        self.fields['equipment_service_date'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_service_date'].label = 'Service Date'
        self.fields['equipment_service_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['equipment_service_hours'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_service_hours'].label = 'Service Hours'
        self.fields['equipment_service_hours'].widget.attrs['style'] = 'width:15ch'

        self.fields['equipment_service_notes'].label = 'Service Notes'
        self.fields['equipment_service_notes'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_service_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = EquipmentServiceRecord
        fields = ['equipment_service_date', 'equipment_service_hours', 'equipment_service_notes']
        widgets = {'equipment_service_date': DateInput()}


class EquipmentServiceRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentServiceRecordUpdateForm, self).__init__(*args, **kwargs)
        self.fields['equipment_service_date'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_service_date'].label = 'Service Date'
        self.fields['equipment_service_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['equipment_service_hours'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_service_hours'].label = 'Service Hours'
        self.fields['equipment_service_hours'].widget.attrs['style'] = 'width:15ch'

        self.fields['equipment_service_notes'].label = 'Service Notes'
        self.fields['equipment_service_notes'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_service_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = EquipmentServiceRecord
        fields = ['equipment_service_date', 'equipment_service_hours', 'equipment_service_notes']
        widgets = {'equipment_service_date': DateInput()}


class EquipmentRepairRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentRepairRecordCreateForm, self).__init__(*args, **kwargs)

        self.fields['equipment_repair_date'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_repair_date'].label = 'Repair Date'
        self.fields['equipment_repair_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['equipment_repair_notes'].label = 'Repair Notes'
        self.fields['equipment_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = EquipmentRepairRecord
        fields = ['equipment_repair_date', 'equipment_repair_notes']
        widgets = {'equipment_repair_date': DateInput()}


class EquipmentRepairRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentRepairRecordUpdateForm, self).__init__(*args, **kwargs)

        self.fields['equipment_repair_date'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_repair_date'].label = 'Repair Date'
        self.fields['equipment_repair_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['equipment_repair_notes'].label = 'Repair Notes'
        self.fields['equipment_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['equipment_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = EquipmentRepairRecord
        fields = ['equipment_repair_date', 'equipment_repair_notes']
        widgets = {'equipment_repair_date': DateInput()}
