from django import forms

from shop.models import Trailer, TrailerServiceRecord, TrailerDotRecord, TrailerRepairRecord

department_choices = (('', 'Select One'),
                      ('10', 'Construction'),
                      ('20', 'Maintenance'),
                      ('50', 'Admin'))


class CreateTrailerForm(forms.ModelForm):
    trailer_department = forms.MultipleChoiceField

    def __init__(self, *args, **kwargs):
        super(CreateTrailerForm, self).__init__(*args, **kwargs)

        self.fields['trailer_license'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_license'].label = 'License#'
        self.fields['trailer_license'].widget.attrs['style'] = 'width:10ch'
        self.fields['trailer_license'].widget.attrs['placeholder'] = 'License'

        self.fields['trailer_vin'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_vin'].label = 'Vin#'
        self.fields['trailer_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['trailer_vin'].widget.attrs['placeholder'] = 'Trailer VIN'

        self.fields['trailer_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_identifier'].label = 'Heritage Equip#'
        self.fields['trailer_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['trailer_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['trailer_department'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_department'].label = 'Heritage Dept#'
        self.fields['trailer_department'].widget.attrs['style'] = 'width:20ch'

        # This adds a size attribute to the html to control the display length
        self.fields['trailer_short_name'].widget.attrs['style'] = 'width:30ch'
        self.fields['trailer_description'].widget.attrs['style'] = 'width:60ch'

    class Meta:
        model = Trailer
        fields = ['trailer_license', 'trailer_vin', 'trailer_identifier',
                  'trailer_department', 'trailer_short_name', 'trailer_description']

        widgets = {'trailer_department': forms.Select(choices=department_choices)}


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateTrailerForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTrailerForm1, self).__init__(*args, **kwargs)

        self.fields['trailer_identifier'].disabled = True
        self.fields['trailer_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_identifier'].label = 'Heritage Equip#'
        self.fields['trailer_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['trailer_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['trailer_license'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_license'].label = 'License#'
        self.fields['trailer_license'].widget.attrs['style'] = 'width:12ch'
        self.fields['trailer_license'].widget.attrs['placeholder'] = 'License'

        self.fields['trailer_vin'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_vin'].label = 'Vin#'
        self.fields['trailer_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['trailer_vin'].widget.attrs['placeholder'] = 'Vehicle VIN'

        # This adds a size attribute to the html to control the display length
        self.fields['trailer_short_name'].label = 'Short Name'
        self.fields['trailer_short_name'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_short_name'].widget.attrs['style'] = 'width:30ch'

        self.fields['trailer_description'].label = 'Description'
        self.fields['trailer_description'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_description'].widget.attrs['style'] = 'width:60ch'

        self.fields['trailer_status'].label = 'Status'
        self.fields['trailer_status'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_status'].widget.attrs['style'] = 'width:15ch'

    class Meta:
        model = Trailer
        fields = ['trailer_identifier', 'trailer_license', 'trailer_vin',
                  'trailer_short_name', 'trailer_description', 'trailer_status']


class UpdateTrailerForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTrailerForm2, self).__init__(*args, **kwargs)

        self.fields['trailer_identifier'].disabled = True
        self.fields['trailer_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_identifier'].label = 'Heritage Equip#'
        self.fields['trailer_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['trailer_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['trailer_service_period'].label = 'Service Period (mos.)'
        self.fields['trailer_service_period'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_service_period'].widget.attrs['style'] = 'width:10ch'

        self.fields['trailer_last_service'].label = 'Last Service'
        self.fields['trailer_last_service'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_last_service'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_next_service'].label = 'Next Service'
        self.fields['trailer_next_service'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_next_service'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = Trailer
        fields = ['trailer_identifier', 'trailer_service_period', 'trailer_last_service', 'trailer_next_service']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']
        widgets = {'trailer_last_service': DateInput(),
                   'trailer_next_service': DateInput(),
                   }


class UpdateTrailerForm3(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTrailerForm3, self).__init__(*args, **kwargs)

        self.fields['trailer_identifier'].disabled = True
        self.fields['trailer_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_identifier'].label = 'Heritage Equip#'
        self.fields['trailer_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['trailer_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['trailer_department'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_department'].label = 'Heritage Dept:'
        self.fields['trailer_department'].widget.attrs['style'] = 'width:20ch'

    class Meta:
        model = Trailer
        fields = ['trailer_identifier', 'trailer_department']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']

        widgets = {'trailer_department': forms.Select(choices=department_choices), }


class UpdateTrailerForm4(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTrailerForm4, self).__init__(*args, **kwargs)

        self.fields['trailer_identifier'].disabled = True
        self.fields['trailer_identifier'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_identifier'].label = 'Heritage Equip#'
        self.fields['trailer_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['trailer_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['trailer_last_dot'].label = 'Last DOT Inspection'
        self.fields['trailer_last_dot'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_last_dot'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_next_dot'].label = 'Next DOT Inspection'
        self.fields['trailer_next_dot'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_next_dot'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_last_dot_status'].label = 'DOT Inspection Status'
        self.fields['trailer_last_dot_status'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_last_dot_status'].widget.attrs['style'] = 'width:16ch'

    class Meta:
        model = Trailer
        fields = ['trailer_identifier', 'trailer_last_dot', 'trailer_next_dot', 'trailer_last_dot_status']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']
        widgets = {'trailer_last_dot': DateInput(),
                   'trailer_next_dot': DateInput(),
                   }


class ServiceRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceRecordCreateForm, self).__init__(*args, **kwargs)

        self.fields['trailer_service_date'].label = 'Trailer Service Date'
        self.fields['trailer_service_date'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_service_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_service_notes'].label = 'Trailer Service Notes'
        self.fields['trailer_service_notes'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_service_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = TrailerServiceRecord
        fields = ['trailer_service_date', 'trailer_service_notes']
        widgets = {'trailer_service_date': DateInput()}


class TrailerServiceRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerServiceRecordUpdateForm, self).__init__(*args, **kwargs)

        self.fields['trailer_service_date'].label = 'Trailer Service Date'
        self.fields['trailer_service_date'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_service_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_service_notes'].label = 'Trailer Service Notes'
        self.fields['trailer_service_notes'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_service_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = TrailerServiceRecord
        fields = ['trailer_service_date', 'trailer_service_notes']
        widgets = {'trailer_service_date': DateInput()}


class TrailerRepairRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerRepairRecordCreateForm, self).__init__(*args, **kwargs)

        self.fields['trailer_repair_date'].label = 'Trailer Repair Date'
        self.fields['trailer_repair_date'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_repair_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_repair_notes'].label = 'Trailer Repair Notes'
        self.fields['trailer_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = TrailerRepairRecord
        fields = ['trailer_repair_date', 'trailer_repair_notes']
        widgets = {'trailer_repair_date': DateInput()}


class TrailerRepairRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerRepairRecordUpdateForm, self).__init__(*args, **kwargs)

        self.fields['trailer_repair_date'].label = 'Trailer Repair Date'
        self.fields['trailer_repair_date'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_repair_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_repair_notes'].label = 'Trailer Repair Notes'
        self.fields['trailer_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

    class Meta:
        model = TrailerRepairRecord
        fields = ['trailer_repair_date', 'trailer_repair_notes']
        widgets = {'trailer_repair_date': DateInput()}


class TrailerDotRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerDotRecordCreateForm, self).__init__(*args, **kwargs)

        self.fields['trailer_dot_inspection_date'].label = 'DOT Inspection Date'
        self.fields['trailer_dot_inspection_date'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_dot_inspection_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_dot_repair_notes'].label = 'DOT Inspection Notes'
        self.fields['trailer_dot_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_dot_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['trailer_dot_passed_inspection'].label = 'DOT Inspection Status'
        self.fields['trailer_dot_passed_inspection'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_dot_passed_inspection'].widget.attrs['style'] = 'width:12ch'

    class Meta:
        model = TrailerDotRecord
        fields = ['trailer_dot_inspection_date', 'trailer_dot_repair_notes', 'trailer_dot_passed_inspection']
        widgets = {'trailer_dot_inspection_date': DateInput()}


class TrailerDotRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerDotRecordUpdateForm, self).__init__(*args, **kwargs)

        self.fields['trailer_dot_inspection_date'].label = 'DOT Inspection Date'
        self.fields['trailer_dot_inspection_date'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_dot_inspection_date'].widget.attrs['style'] = 'width:16ch'

        self.fields['trailer_dot_repair_notes'].label = 'DOT Inspection Notes'
        self.fields['trailer_dot_repair_notes'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_dot_repair_notes'].widget.attrs['style'] = 'width:60ch;height:14ch'

        self.fields['trailer_dot_passed_inspection'].label = 'DOT Inspection Status'
        self.fields['trailer_dot_passed_inspection'].widget.attrs['class'] = 'form-control'
        self.fields['trailer_dot_passed_inspection'].widget.attrs['style'] = 'width:12ch'

    class Meta:
        model = TrailerDotRecord
        fields = ['trailer_dot_inspection_date', 'trailer_dot_repair_notes', 'trailer_dot_passed_inspection']
        widgets = {'trailer_dot_inspection_date': DateInput()}

