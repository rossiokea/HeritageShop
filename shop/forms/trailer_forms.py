from django import forms

from shop.models import Trailer, TrailerServiceRecord, TrailerDotRecord, TrailerRepairRecord


class CreateTrailerForm(forms.ModelForm):
    trailer_department = forms.MultipleChoiceField

    def __init__(self, *args, **kwargs):
        super(CreateTrailerForm, self).__init__(*args, **kwargs)

        self.fields['trailer_license'].widget.attrs['class'] = 'form-group'
        self.fields['trailer_license'].label = 'License#'
        self.fields['trailer_license'].widget.attrs['style'] = 'width:10ch'
        self.fields['trailer_license'].widget.attrs['placeholder'] = 'License'

        self.fields['trailer_vin'].widget.attrs['class'] = 'form-group'
        self.fields['trailer_vin'].label = 'Vin#'
        self.fields['trailer_vin'].widget.attrs['style'] = 'width:27ch'
        self.fields['trailer_vin'].widget.attrs['placeholder'] = 'Trailer VIN'

        self.fields['trailer_identifier'].widget.attrs['class'] = 'form-group'
        self.fields['trailer_identifier'].label = 'Heritage Equip#'
        self.fields['trailer_identifier'].widget.attrs['style'] = 'width:15ch'
        self.fields['trailer_identifier'].widget.attrs['placeholder'] = 'XXX'

        self.fields['trailer_department'].widget.attrs['class'] = 'form-group'
        self.fields['trailer_department'].label = 'Heritage Dept#'
        self.fields['trailer_department'].widget.attrs['style'] = 'width:20ch'

    class Meta:
        department_choices = (('', 'Select One'),
                              ('10', 'Construction'),
                              ('20', 'Maintenance'),
                              ('50', 'Admin'))
        model = Trailer
        fields = ['trailer_license', 'trailer_vin', 'trailer_identifier',
                  'trailer_department', 'trailer_short_name', 'trailer_description']

        widgets = {'trailer_department': forms.Select(choices=department_choices)}


class DateInput(forms.DateInput):
    input_type = 'date'


class UpdateTrailerForm1(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTrailerForm1, self).__init__(*args, **kwargs)

    class Meta:
        model = Trailer
        fields = ['trailer_license', 'trailer_vin', 'trailer_identifier',
                  'trailer_short_name', 'trailer_description', 'trailer_status']


class UpdateTrailerForm2(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTrailerForm2, self).__init__(*args, **kwargs)

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

    class Meta:
        model = Trailer
        fields = ['trailer_identifier', 'trailer_department']
        # fields = ['service_period', 'last_service', 'last_service_miles',
        #        'next_service']


class UpdateTrailerForm4(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UpdateTrailerForm4, self).__init__(*args, **kwargs)

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

    class Meta:
        model = TrailerServiceRecord
        fields = ['trailer_service_date', 'trailer_service_notes']
        widgets = {'trailer_service_date': DateInput()}


class TrailerServiceRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerServiceRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TrailerServiceRecord
        fields = ['trailer_service_date', 'trailer_service_notes']
        widgets = {'trailer_service_date': DateInput()}


class TrailerRepairRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerRepairRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TrailerRepairRecord
        fields = ['trailer_repair_date', 'trailer_repair_notes']
        widgets = {'trailer_repair_date': DateInput()}


class TrailerRepairRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerRepairRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TrailerRepairRecord
        fields = ['trailer_repair_date', 'trailer_repair_notes']
        widgets = {'trailer_repair_date': DateInput()}


class TrailerDotRecordCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerDotRecordCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TrailerDotRecord
        fields = ['trailer_dot_inspection_date', 'trailer_dot_repair_notes', 'trailer_dot_passed_inspection']
        widgets = {'trailer_dot_inspection_date': DateInput()}


class TrailerDotRecordUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrailerDotRecordUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TrailerDotRecord
        fields = ['trailer_dot_inspection_date', 'trailer_dot_repair_notes', 'trailer_dot_passed_inspection']
        widgets = {'trailer_dot_inspection_date': DateInput()}

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
