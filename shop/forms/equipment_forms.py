from django import forms

from shop.models import Equipment, EquipmentServiceRecord, EquipmentRepairRecord, Trailer, TrailerServiceRecord, \
    TrailerDotRecord, TrailerRepairRecord


class CreateEquipmentForm(forms.ModelForm):
    equipment_department = forms.MultipleChoiceField

    def __init__(self, *args, **kwargs):
        super(CreateEquipmentForm, self).__init__(*args, **kwargs)

        self.fields['equipment_vin'].widget.attrs['class'] = 'form-group'
        self.fields['equipment_vin'].label = 'Vin#'
        self.fields['equipment_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['equipment_vin'].widget.attrs['placeholder'] = 'Equipment VIN'

        self.fields['equipment_identifier'].widget.attrs['class'] = 'form-group'
        self.fields['equipment_identifier'].label = 'Heritage Equip#'
        self.fields['equipment_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['equipment_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['equipment_department'].widget.attrs['class'] = 'form-group'
        self.fields['equipment_department'].label = 'Heritage Dept#'
        self.fields['equipment_department'].widget.attrs['style'] = 'width:20ch'

    class Meta:
        department_choices = (('', 'Select One'),
                              ('10', 'Construction'),
                              ('20', 'Maintenance'),
                              ('50', 'Admin'))
        model = Equipment
        fields = ['equipment_vin', 'equipment_identifier',
                  'equipment_department', 'equipment_short_name', 'equipment_description']

        widgets = {'equipment_department': forms.Select(choices=department_choices)}


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateEquipmentForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateEquipmentForm1, self).__init__(*args, **kwargs)

    class Meta:
        model = Equipment
        fields = ['equipment_vin', 'equipment_identifier',
                  'equipment_short_name', 'equipment_description', 'equipment_status']


class UpdateEquipmentForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateEquipmentForm2, self).__init__(*args, **kwargs)

    class Meta:
        model = Equipment
        fields = ['equipment_service_period', 'equipment_last_service_hours', 'equipment_next_service_hours',
                  'equipment_last_service', 'equipment_next_service']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']
        widgets = {'equipment_last_service': DateInput(),
                   'equipment_next_service': DateInput(),
                   }


class UpdateEquipmentForm3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateEquipmentForm3, self).__init__(*args, **kwargs)

    class Meta:
        model = Equipment
        fields = ['equipment_department', 'equipment_assigned_employee', 'equipment_assigned_project']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']


class ServiceRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EquipmentServiceRecord
        fields = ['equipment_service_date', 'equipment_service_hours', 'equipment_service_notes']
        widgets = {'equipment_service_date': DateInput()}


class EquipmentServiceRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentServiceRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EquipmentServiceRecord
        fields = ['equipment_service_date', 'equipment_service_hours', 'equipment_service_notes']
        widgets = {'equipment_service_date': DateInput()}


class EquipmentRepairRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentRepairRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EquipmentRepairRecord
        fields = ['equipment_repair_date', 'equipment_repair_notes']
        widgets = {'equipment_repair_date': DateInput()}


class EquipmentRepairRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentRepairRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EquipmentRepairRecord
        fields = ['equipment_repair_date', 'equipment_repair_notes']
        widgets = {'equipment_repair_date': DateInput()}


'''
class UpdateEquipmentForm4(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateEquipmentForm4, self).__init__(*args, **kwargs)

    class Meta:
        model = Equipment
        fields = ['equipment_last_dot', 'trailer_next_dot', 'trailer_last_dot_status']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']
        widgets = {'trailer_last_dot': DateInput(),
                   'trailer_next_dot': DateInput(),
                   }
'''

'''
class EquipmentDotRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentDotRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EquipmentDotRecord
        fields = ['trailer_dot_inspection_date', 'trailer_dot_repair_notes', 'trailer_dot_passed_inspection']
        widgets = {'trailer_dot_inspection_date': DateInput()}
'''
'''
class EquipmentDotRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EquipmentDotRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = EquipmentDotRecord
        fields = ['trailer_dot_inspection_date', 'trailer_dot_repair_notes', 'trailer_dot_passed_inspection']
        widgets = {'trailer_dot_inspection_date': DateInput()}

'''
