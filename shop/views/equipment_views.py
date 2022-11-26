import datetime
from datetime import timedelta
from shop.models import Equipment
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q, F

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms.equipment_forms import *
from shop.models import Equipment, EquipmentServiceRecord, EquipmentRepairRecord


# Create your views here.
######################################
# Equipment Related Views
######################################

class EquipmentListView(ListView):
    model = Equipment
    template_name = 'shop/equipment_list.html'
    queryset = Equipment.objects.all().order_by(F('equipment_next_service').asc(nulls_last=True)).filter(
        equipment_status=True)

    # context_object_name = 'vehicle_list'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context_mod = super(EquipmentListView, self).get_context_data(**kwargs)

        # Get the Vehicles
        vehicles = Equipment.objects.all().order_by(F('equipment_next_service').asc(nulls_last=True)).filter(
            equipment_status=True)

        # *************Paginating the VEHICLE DATA ****************
        # Paginate The List
        paginated_vehicles = Paginator(vehicles, 9)
        page_number = self.request.GET.get('page')
        vehicles_page_obj = paginated_vehicles.get_page(page_number)
        # Add Paginated data to context
        context_mod['equipment_page_obj'] = vehicles_page_obj
        # ************* END Paginating the VEHICLE DATA ****************

        # Set the Active Tab
        context_mod['vehicle_nav'] = ''
        context_mod['trailer_nav'] = ''
        context_mod['equipment_nav'] = 'active'
        context_mod['service_nav'] = ''
        context_mod['dot_nav'] = ''

        # context_mod['vehicle_list'] = vehicles

        context_mod['today'] = datetime.date.today()
        context_mod['today_20'] = datetime.date.today() + timedelta(14)
        print(f"The Equipment List Context is: {context_mod}")
        return context_mod


# This Main be Absolete as all Records Views are handled throught the Vehicle, Trailer, Equipment Views

class EquipmentCreateView(CreateView):
    form_class = CreateEquipmentForm
    # model = Vehicle
    template_name = 'shop/equipment_create_form.html'

    # fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
    #         'vehicle_department', 'vehicle_short_name', 'vehicle_description']

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_list")
        # return reverse("shop:list_vehicles")


class EquipmentDetailsView(DetailView):
    model = Equipment
    template_name = 'shop/equipment_details.html'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(EquipmentDetailsView, self).get_context_data(**kwargs)
        # context2 = ServiceListView.get_context_data(*kwargs)
        # print(context2)

        print("Getting Equipment Service Records")
        # Get the Service Records
        service_records = EquipmentServiceRecord.objects.filter(equipment=self.kwargs['pk']).select_related(
            'equipment').order_by('equipment_service_date').reverse()
        print(f"The equipment service records are: {service_records}")
        # Paginate the Service Records:
        paginated_service_records = Paginator(service_records, 7)
        page_number = self.request.GET.get('page')
        service_records_page_obj = paginated_service_records.get_page(page_number)
        # Add the Service Records to the context
        context["service_records"] = service_records
        context['service_records_page_obj'] = service_records_page_obj

        # Get the Repair Records

        repair_records = EquipmentRepairRecord.objects.filter(equipment=self.kwargs['pk']).select_related(
            'equipment').order_by('equipment_repair_date').reverse()
        # Paginate the Service Records:
        paginated_repair_records = Paginator(repair_records, 7)
        repair_page_number = self.request.GET.get('page')
        repair_records_page_obj = paginated_repair_records.get_page(repair_page_number)
        # Add the Service Records to the context
        context["repair_records"] = repair_records
        context['repair_records_page_obj'] = repair_records_page_obj

        # Get the DOT Inspection Records
        '''
        dot_records = EquipmentDotRecord.objects.filter(equipment=self.kwargs['pk']).select_related(
            'equipment').order_by('equipment_dot_inspection_date').reverse()
        # Paginate the Service Records:
        print(f"The Dot Records\n{dot_records}")
        paginated_dot_records = Paginator(dot_records, 7)
        dot_page_number = self.request.GET.get('page')
        dot_records_page_obj = paginated_dot_records.get_page(dot_page_number)
        # Add the Service Records to the context

        context["dot_records"] = dot_records
        context['dot_records_page_obj'] = dot_records_page_obj
        '''
        # Set the Active Tab
        context['vehicle_nav'] = ''
        context['trailer_nav'] = ''
        context['equipment_nav'] = 'active'
        context['service_nav'] = ''
        context['dot_nav'] = ''

        return context


# override context data
# def get_context_data(self, *args, **kwargs):
#     service_records = VehicleServiceRecord.objects.filter(vehicle=self.kwargs['pk']).select_related('vehicle')
#     context = super(ServiceListView, self).get_context_data(**kwargs)
#     # add extra field
#     context["service_records"] = service_records
#     return context
# def paginate_queryset(self, queryset, page_size):
#     service_records = VehicleServiceRecord.objects.filter(vehicle=self.kwargs['pk']).select_related('vehicle')
#     return service_records
#
# def get_queryset(self, *args, **kwargs):
#     service_records = VehicleServiceRecord.objects.filter(vehicle=self.kwargs['pk']).select_related('vehicle')
#     service_records = 'junk'
#     paginated = Paginator(service_records, 3)
#     print("I am in servicerecords queryset")
#     print(paginated.page(1))
#     return service_records

class EquipmentUpdate1(UpdateView):
    form_class = UpdateEquipmentForm1
    template_name = 'shop/equipment_update_form.html'

    # success_url = reverse_lazy('shop:detail_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Equipment.objects.get(equipment_id=self.kwargs['pk'])
        return obj


class EquipmentUpdate2(UpdateView):
    form_class = UpdateEquipmentForm2
    template_name = 'shop/equipment_update_form.html'

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Equipment.objects.get(equipment_id=self.kwargs['pk'])
        return obj


class EquipmentUpdate3(UpdateView):
    form_class = UpdateEquipmentForm3
    template_name = 'shop/equipment_update_form.html'

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Equipment.objects.get(equipment_id=self.kwargs['pk'])
        return obj


'''
class EquipmentUpdate4(UpdateView):
    form_class = UpdateEquipmentForm4
    template_name = 'shop/equipment_update_form.html'

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Equipment.objects.get(eqiupment_id=self.kwargs['pk'])
        return obj

'''


class EquipmentSearchListView(ListView):
    model = Equipment
    template_name = 'shop/equipment_list.html'

    def get_queryset(self):
        print('Entering Equipment get_queryset')
        qsearch = self.request.GET.get('q')
        dsearch = self.request.GET.get('department')
        status = self.request.GET.get('item_status')

        # Set the dsearch to blank if a None is returned since query does not handle None
        if dsearch is None:
            dsearch = ""

        print(f"Q is: {qsearch}\nDepartment is: {dsearch}\nStatus is: {status}")

        # Perform the base query to select either active or inactive vehicles
        if status == 'Active':
            print(f"Searching for {status} Equipment")
            queryset_status = Equipment.objects.all().order_by(F('equipment_next_service').asc(nulls_last=True)).filter(
                equipment_status=True)
        else:
            print(f"Searching for {status} Equipment")
            queryset_status = Equipment.objects.all().order_by(F('equipment_next_service').asc(nulls_last=True)).filter(
                equipment_status=False)

        if dsearch and not qsearch:
            print(f"Hello I am in department only: {dsearch}")
            queryset = queryset_status.filter(equipment_department=dsearch).order_by('equipment_next_service')
            print(queryset)
            return queryset

        elif qsearch and not dsearch:
            print("Getting result for text search only")
            q_short_des = Q(equipment_short_name__icontains=qsearch)
            q_assigned = Q(equipment_assigned_employee__icontains=qsearch)
            q_des = Q(equipment_description__icontains=qsearch)
            q_id = Q(equipment_identifier__icontains=qsearch)
            queryset = queryset_status.filter(Q(q_short_des | q_assigned | q_des | q_id))

            return queryset

        elif qsearch and dsearch:
            print('Getting search for Both Q and Department')
            queryset = queryset_status.filter(
                Q(Q(equipment_short_name__icontains=qsearch) |
                  Q(equipment_assigned_employee__icontains=qsearch) |
                  Q(equipment_description__icontains=qsearch)) &
                Q(equipment_department=dsearch))
            return queryset
        else:
            print("There was no q")

        # Return the Initial Query since there was no department or q selected
        return queryset_status.order_by('equipment_next_service')

    def get_context_data(self, *args, **kwargs):
        context_mod = super(EquipmentSearchListView, self).get_context_data(**kwargs)

        # Get the Query Set from the get_query set function
        equipment = self.get_queryset().order_by(F('equipment_next_service').asc(nulls_last=True))
        print(f"The Equipment Object is: {equipment.count()}")
        # *************Paginating the VEHICLE DATA ****************
        # Paginate The List
        paginated_equipment = Paginator(equipment, 9)
        page_number = self.request.GET.get('page')
        equipment_page_obj = paginated_equipment.get_page(page_number)
        # Add Paginated data to context
        context_mod['equipment_page_obj'] = equipment_page_obj
        print(f"The Equipment Page data is: {equipment_page_obj}")
        # ************* END Paginating the VEHICLE DATA ****************

        # Add Search Releated Items to Context
        context_mod['selected_item_status'] = self.request.GET.get('item_status')
        context_mod['selected_department'] = self.request.GET.get("department")
        context_mod['search_text'] = self.request.GET.get('q')
        context_mod['selected_q'] = self.request.GET.get("q")

        context_mod['trailer_nav'] = ''
        context_mod['vehicle_nav'] = ''
        context_mod['equipment_nav'] = 'active'
        context_mod['service_nav'] = ''
        context_mod['dot_nav'] = ''

        # context['vehicle_list'] = queryset
        # context_mod['vehicle_list'] = vehicles

        context_mod['today'] = datetime.date.today()
        context_mod['today_20'] = datetime.date.today() + timedelta(14)
        print(f"The Equipment Search Context is: {context_mod}")
        return context_mod


class EquipmentServiceRecordCreateView(CreateView):
    form_class = ServiceRecordCreateForm
    # model = Vehicle
    template_name = 'shop/equipment_service_record_create_form.html'

    # fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
    #         'vehicle_department', 'vehicle_short_name', 'vehicle_description']

    # success_url = reverse_lazy('shop:list_vehicles')

    def form_valid(self, form):
        form.instance.equipment_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(form.cleaned_data.get('equipment_service_date'))
        print(f"The Service Record Hours is data is {form.cleaned_data.get('equipment_service_hours')}")
        # Grab the data from the service form
        date = form.cleaned_data.get('equipment_service_date')

        # Get the Current equipment we are working on
        equipment = Equipment.objects.get(pk=self.kwargs.get('pk'))
        try:
            # Calculate the next service date
            service_period = equipment.equipment_service_period
            print(f"Service type is {type(service_period)}")
            if service_period is None:
                print(f"I found service_period is none {service_period}")
                service_period = 300
                equipment.equipment_service_period = service_period
            next_service = date + timedelta(weeks=(52))

            print(next_service)
            # Update the current service hours for the equipment object
            equipment.equipment_last_service_hours = int(form.cleaned_data.get('equipment_service_hours'))
            equipment.equipment_next_service_hours = int(form.cleaned_data.get('equipment_service_hours')) + int(
                service_period)
            equipment.equipment_last_service = date
            equipment.equipment_next_service = next_service
            # save to database
            equipment.save()
        except Exception as e:
            print(f"The Exception is: {e}")

        # print(next_service, type(next_service))

        # Update all the service info

        return super(EquipmentServiceRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Equipment.objects.get(equipment_id=self.kwargs['pk'])
        return obj


class EquipmentServiceRecordDeleteView(DeleteView):
    model = EquipmentServiceRecord
    success_url = 'shop/equipment_details.html'
    template_name = 'shop/vehicle_service_record_delete_form.html'

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        service_record = EquipmentServiceRecord.objects.filter(id=self.kwargs['id'])
        print(service_record)
        return service_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class EquipmentServiceRecordUpdateView(UpdateView):
    form_class = EquipmentServiceRecordUpdateForm
    template_name = 'shop/equipment_service_record_update_form.html'

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        service_record = EquipmentServiceRecord.objects.filter(id=self.kwargs['id']).first()
        print(service_record)
        return service_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


# #####################Repair Record Related Views ########################3

class EquipmentRepairRecordCreateView(CreateView):
    form_class = EquipmentRepairRecordCreateForm
    # model = Vehicle
    template_name = 'shop/equipment_repair_record_create_form.html'

    # fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
    #         'vehicle_department', 'vehicle_short_name', 'vehicle_description']

    # success_url = reverse_lazy('shop:list_vehicles')

    def form_valid(self, form):
        form.instance.equipment_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(form.cleaned_data.get('equipment_repair_date'))

        # Grab the data from the service form
        date = form.cleaned_data.get('equipment_repair_date')

        # Get the Current Vehicle we are working on
        equipment = Equipment.objects.get(pk=self.kwargs.get('pk'))
        try:
            # Calculate the next service date
            service_period = equipment.service_period
            print(f"Service type is {type(service_period)}")
            if service_period is None:
                print(f"I found service_period is none {service_period}")
                service_period = 6
                equipment.service_period = service_period
            next_service = date + timedelta(weeks=(service_period * 4))

            print(next_service)
            equipment.next_service = next_service
            equipment.last_service = date

            # save to database
            equipment.save()
        except Exception as e:
            print(e)

        # print(next_service, type(next_service))

        # Update all the service info

        return super(EquipmentRepairRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Equipment.objects.get(equipment_id=self.kwargs['pk'])
        return obj


class EquipmentRepairRecordUpdateView(UpdateView):
    form_class = EquipmentRepairRecordUpdateForm
    template_name = 'shop/equipment_repair_record_update_form.html'

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        repair_record = EquipmentRepairRecord.objects.filter(id=self.kwargs['id']).first()
        print(repair_record)
        return repair_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class EquipmentRepairRecordDeleteView(DeleteView):
    model = EquipmentServiceRecord
    success_url = 'shop/equipment_details.html'
    template_name = 'shop/equipment_repair_record_delete_form.html'

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        repair_record = EquipmentRepairRecord.objects.filter(id=self.kwargs['id'])
        print(repair_record)
        return repair_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


# ##################### DOT Record Related Views ########################3
'''
class EquipmentDotRecordCreateView(CreateView):
    form_class = EquipmentDotRecordCreateForm
    template_name = 'shop/equipment_dot_record_create_form.html'

    # fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
    #         'vehicle_department', 'vehicle_short_name', 'vehicle_description']

    def form_valid(self, form):
        form.instance.equipment_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(f"the Cleaned data is{form.cleaned_data}")

        # Grab the data from the service form
        date = form.cleaned_data.get('equipment_dot_inspection_date')
        print(f"The Equipment Inspection Date is: {date}")

        # Get the Current Vehicle we are working on
        equipment = Equipment.objects.get(pk=self.kwargs.get('pk'))
        print(f"The Equipment is: {equipment}")
        # Update the dates for DOT stuff
        try:
            # Calculate the next DOT inspection date
            dot_period = 12
            print(f"Dot type is {type(dot_period)}")
            if dot_period is None:
                print(f"I found dot_period is none {dot_period}")
                service_period = 12

            next_dot = date + timedelta(weeks=(dot_period * 4))

            print(next_dot)
            equipment.equipment_next_dot = next_dot
            equipment.equipment_last_dot = date

            # save to database
            equipment.save()
        except Exception as e:
            print(e)

        return super(EquipmentDotRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Equipment.objects.get(equipment_id=self.kwargs['pk'])
        return obj
'''
'''
class EquipmentDotRecordUpdateView(UpdateView):
    form_class = EquipmentDotRecordUpdateForm
    template_name = 'shop/equipment_dot_record_update_form.html'

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        dot_record = EquipmentDotRecord.objects.filter(id=self.kwargs['id']).first()
        print(dot_record)
        return dot_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")
'''
'''
class EquipmentDotRecordDeleteView(DeleteView):
    model = EquipmentDotRecord
    success_url = 'shop/equipment_details.html'
    template_name = 'shop/equipment_dot_record_delete_form.html'

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        dot_record = EquipmentDotRecord.objects.filter(id=self.kwargs['id'])
        print(dot_record)
        return dot_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:equipment_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")
'''
######################################
# Equipment Related Views
######################################
