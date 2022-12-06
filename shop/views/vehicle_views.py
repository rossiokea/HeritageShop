import datetime
import operator
from datetime import timedelta

from django.http import HttpResponse

from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import context
from django.urls import reverse_lazy
from django.db.models import Q, F

from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView

import shop.forms.vehicle_forms
# from shop.models import Vehicle, Trailer, Equipment, \
#    VehicleServiceRecord, VehicleRepairRecord, VehicleDotRecord
from shop.models import *

from shop.forms.vehicle_forms import *
from shop.forms.trailer_forms import *

from itertools import chain


# Create your views here.

def home_page(request):
    return render(request, 'shop/home.html')


######################################
# Vehicle Related Views
######################################

class ListVehiclesView(ListView):
    model = Vehicle
    template_name = 'shop/vehicles_list.html'
    queryset = Vehicle.objects.all().order_by(F('next_service').asc(nulls_last=True)).filter(vehicle_status=True)

    # context_object_name = 'vehicle_list'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context_mod = super(ListVehiclesView, self).get_context_data(**kwargs)

        # Get the Vehicles
        vehicles = Vehicle.objects.all().order_by(F('next_service').asc(nulls_last=True)).filter(vehicle_status=True)

        # *************Paginating the VEHICLE DATA ****************
        # Paginate The List
        paginated_vehicles = Paginator(vehicles, 9)
        page_number = self.request.GET.get('page')
        vehicles_page_obj = paginated_vehicles.get_page(page_number)
        # Add Paginated data to context
        context_mod['vehicles_page_obj'] = vehicles_page_obj
        # ************* END Paginating the VEHICLE DATA ****************

        # Set the Active Tab
        context_mod['vehicle_nav'] = 'active'
        context_mod['trailer_nav'] = ''
        context_mod['equipment_nav'] = ''
        context_mod['dot_nav'] = ''

        context_mod['vehicle_list'] = vehicles

        context_mod['today'] = datetime.date.today()
        context_mod['today_20'] = datetime.date.today() + timedelta(14)
        print(f"The Vehicle List Context is: {context_mod}")
        return context_mod


class VehicleDetailsView(DetailView):
    model = Vehicle
    template_name = 'shop/vehicles_details.html'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(VehicleDetailsView, self).get_context_data(**kwargs)
        # context2 = ServiceListView.get_context_data(*kwargs)
        # print(context2)

        # Get the Service Records
        service_records = VehicleServiceRecord.objects.filter(vehicle=self.kwargs['pk']).select_related(
            'vehicle').order_by('service_date').reverse()
        # Paginate the Service Records:
        paginated_service_records = Paginator(service_records, 7)
        page_number = self.request.GET.get('page')
        service_records_page_obj = paginated_service_records.get_page(page_number)
        # Add the Service Records to the context
        context["service_records"] = service_records
        context['service_records_page_obj'] = service_records_page_obj

        # Get the Repair Records

        repair_records = VehicleRepairRecord.objects.filter(vehicle=self.kwargs['pk']).select_related(
            'vehicle').order_by('repair_date').reverse()
        # Paginate the Service Records:
        paginated_repair_records = Paginator(repair_records, 7)
        repair_page_number = self.request.GET.get('page')
        repair_records_page_obj = paginated_repair_records.get_page(repair_page_number)
        # Add the Service Records to the context
        context["repair_records"] = repair_records
        context['repair_records_page_obj'] = repair_records_page_obj

        # Get the DOT Inspection Records
        dot_records = VehicleDotRecord.objects.filter(vehicle=self.kwargs['pk']).select_related(
            'vehicle').order_by('dot_inspection_date').reverse()
        # Paginate the Service Records:
        print(f"The Dot Records\n{dot_records}")
        paginated_dot_records = Paginator(dot_records, 7)
        dot_page_number = self.request.GET.get('page')
        dot_records_page_obj = paginated_dot_records.get_page(dot_page_number)
        # Add the Service Records to the context

        context["dot_records"] = dot_records
        context['dot_records_page_obj'] = dot_records_page_obj

        # Set the Active Tab
        context['vehicle_nav'] = 'active'
        context['trailer_nav'] = ''
        context['equipment_nav'] = ''
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


class VehicleCreateView(CreateView):
    form_class = shop.forms.vehicle_forms.CreateVehicleForm
    # model = Vehicle
    template_name = 'shop/vehicle_create_form.html'

    # fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
    #         'vehicle_department', 'vehicle_short_name', 'vehicle_description']

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:vehicles_list")
        # return reverse("shop:list_vehicles")


class VehicleUpdate1(UpdateView):
    form_class = shop.forms.vehicle_forms.UpdateVehicleForm1
    template_name = 'shop/vehicle_update_form.html'
    pk_url_kwarg = Vehicle.vehicle_id

    # success_url = reverse_lazy('shop:detail_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Vehicle.objects.get(vehicle_id=self.kwargs['pk'])
        return obj

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(VehicleUpdate1, self).get_form_kwargs()
        print(f"The kwargs are: {kwargs}")
        return kwargs


class VehicleUpdate2(UpdateView):
    form_class = shop.forms.vehicle_forms.UpdateVehicleForm2
    template_name = 'shop/vehicle_update_form.html'
    pk_url_kwarg = Vehicle.vehicle_id

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Vehicle.objects.get(vehicle_id=self.kwargs['pk'])
        return obj

    # This View has been moved to the MainSection
    # class VehicleUpdate3(UpdateView):
    #     form_class = shop.forms.vehicle_forms.UpdateVehicleForm3
    #     template_name = 'shop/vehicle_update_form.html'
    #     pk_url_kwarg = Vehicle.vehicle_id

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Vehicle.objects.get(vehicle_id=self.kwargs['pk'])
        return obj


class VehicleUpdate4(UpdateView):
    form_class = shop.forms.vehicle_forms.UpdateVehicleForm4
    template_name = 'shop/vehicle_update_form.html'
    pk_url_kwarg = Vehicle.vehicle_id

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Vehicle.objects.get(vehicle_id=self.kwargs['pk'])
        return obj


class SearchListVehiclesView(ListView):
    model = Vehicle
    template_name = 'shop/vehicles_list.html'

    def get_queryset(self):
        print('Entering Vehicle get_queryset')
        qsearch = self.request.GET.get('q')
        dsearch = self.request.GET.get('department')
        status = self.request.GET.get('item_status')

        # Set the dsearch to blank if a None is returned since query does not handle None
        if dsearch is None:
            dsearch = ""

        print(f"Q is: {qsearch}\nDepartment is: {dsearch}\nStatus is: {status}")

        # Perform the enhanced Query for when other search items selected in the query
        if status == 'Active':
            print(f"Searching for {status} Vehicles")
            queryset_status = Vehicle.objects.all().order_by(F('vehicle_identifier').asc(nulls_last=True)).filter(
                vehicle_status=True)
        else:
            print(f"Searching for {status} Vehicles")
            queryset_status = Vehicle.objects.all().order_by(F('vehicle_identifier').asc(nulls_last=True)).filter(
                vehicle_status=False)

        if dsearch and not qsearch:
            print(f"Hello I am in department only: {dsearch}")
            queryset = queryset_status.filter(vehicle_department=dsearch).order_by('vehicle_identifier')
            print(queryset)
            return queryset

        elif qsearch and not dsearch:
            print("Getting result for text search only")
            q_short_des = Q(vehicle_short_name__icontains=qsearch)
            q_assigned = Q(assigned_employee__icontains=qsearch)
            q_des = Q(vehicle_description__icontains=qsearch)
            q_id = Q(vehicle_identifier__icontains=qsearch)
            q_license = Q(vehicle_license__icontains=qsearch)
            queryset = queryset_status.filter(Q(q_short_des | q_assigned | q_des | q_id | q_license)).order_by(
                'vehicle_identifier')

            return queryset

        elif qsearch and dsearch:
            print('Getting search for Both Q and Department')
            queryset = queryset_status.filter(
                Q(Q(vehicle_short_name__icontains=qsearch) |
                  Q(assigned_employee__icontains=qsearch) |
                  Q(vehicle_description__icontains=qsearch) |
                  Q(vehicle_license__icontains=qsearch)) &
                Q(vehicle_department=dsearch)).order_by('vehicle_identifier')
            return queryset
        else:
            print("There was no q")

        # Return the Initial Query since there was no department or q selected
        return queryset_status.order_by('vehicle_identifier')

    def get_context_data(self, *args, **kwargs):
        context_mod = super(SearchListVehiclesView, self).get_context_data(**kwargs)

        # Get the Query Set from the get_query set function and select the order by
        vehicles = self.get_queryset().order_by(F('vehicle_identifier').asc(nulls_last=True))
        print(f"The Vehicles Object is: {vehicles.count()}")
        # *************Paginating the VEHICLE DATA ****************
        # Paginate The List
        NUM_ITEMS_PAGE = 9
        paginated_vehicles = Paginator(vehicles, NUM_ITEMS_PAGE)
        page_number = self.request.GET.get('page')
        vehicles_page_obj = paginated_vehicles.get_page(page_number)
        # Add Paginated data to context
        context_mod['vehicles_page_obj'] = vehicles_page_obj
        print(f"The Vehicle Page data is: {vehicles_page_obj}")
        # ************* END Paginating the VEHICLE DATA ****************
        # Add Search Releated Items to Context
        context_mod['selected_item_status'] = self.request.GET.get('item_status')
        context_mod['selected_department'] = self.request.GET.get("department")
        context_mod['search_text'] = self.request.GET.get('q')
        context_mod['selected_q'] = self.request.GET.get("q")

        context_mod['trailer_nav'] = ''
        context_mod['vehicle_nav'] = 'active'
        context_mod['equipment_nav'] = ''
        context_mod['service_nav'] = ''

        # context['vehicle_list'] = queryset
        # context_mod['vehicle_list'] = vehicles

        context_mod['today'] = datetime.date.today()
        context_mod['today_20'] = datetime.date.today() + timedelta(14)
        print(f"The Vehicle Search Context is: {context_mod}")
        return context_mod


class ServiceRecordCreateView(CreateView):
    form_class = shop.forms.vehicle_forms.ServiceRecordCreateForm
    # model = Vehicle
    template_name = 'shop/vehicle_service_record_create_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def form_valid(self, form):
        form.instance.vehicle_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(form.cleaned_data.get('service_date'))

        # Grab the data from the service form
        date = form.cleaned_data.get('service_date')
        miles = form.cleaned_data.get('service_miles')

        # Get the Current Vehicle we are working on
        vehicle = Vehicle.objects.get(pk=self.kwargs.get('pk'))
        try:
            # Calculate the next service date
            service_period = vehicle.service_period
            print(f"Service type is {type(service_period)}")
            if service_period is None:
                print(f"I found service_period is none {service_period}")
                service_period = 6
                vehicle.service_period = service_period
            next_service = date + timedelta(weeks=(service_period * 4))

            print(next_service)
            vehicle.next_service = next_service
            vehicle.last_service = date
            vehicle.last_service_miles = miles

            # save to database
            vehicle.save()
        except Exception as e:
            print(e)

        # print(next_service, type(next_service))

        # Update all the service info

        return super(ServiceRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Vehicle.objects.get(vehicle_id=self.kwargs['pk'])
        return obj


class ServiceRecordDeleteView(DeleteView):
    model = VehicleServiceRecord
    success_url = 'shop/vehicles_details.html'
    template_name = 'shop/vehicle_service_record_delete_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        service_record = VehicleServiceRecord.objects.filter(id=self.kwargs['id'])
        print(service_record)
        return service_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class ServiceRecordUpdateView(UpdateView):
    form_class = shop.forms.vehicle_forms.ServiceRecordUpdateForm
    template_name = 'shop/vehicle_service_record_update_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        service_record = VehicleServiceRecord.objects.filter(id=self.kwargs['id']).first()
        print(service_record)
        return service_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


# #####################Repair Record Related Views ########################3

class RepairRecordCreateView(CreateView):
    form_class = shop.forms.vehicle_forms.RepairRecordCreateForm
    # model = Vehicle
    template_name = 'shop/vehicle_repair_record_create_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def form_valid(self, form):
        form.instance.vehicle_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(form.cleaned_data.get('service_date'))

        # Grab the data from the service form
        date = form.cleaned_data.get('service_date')
        miles = form.cleaned_data.get('service_miles')

        # Get the Current Vehicle we are working on
        vehicle = Vehicle.objects.get(pk=self.kwargs.get('pk'))
        try:
            # Calculate the next service date
            service_period = vehicle.service_period
            print(f"Service type is {type(service_period)}")
            if service_period is None:
                print(f"I found service_period is none {service_period}")
                service_period = 6
                vehicle.service_period = service_period
            next_service = date + timedelta(weeks=(service_period * 4))

            print(next_service)
            vehicle.next_service = next_service
            vehicle.last_service = date
            vehicle.last_service_miles = miles

            # save to database
            vehicle.save()
        except Exception as e:
            print(e)

        # print(next_service, type(next_service))

        # Update all the service info

        return super(RepairRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Vehicle.objects.get(vehicle_id=self.kwargs['pk'])
        return obj


class RepairRecordUpdateView(UpdateView):
    form_class = shop.forms.vehicle_forms.RepairRecordUpdateForm
    template_name = 'shop/vehicle_repair_record_update_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        repair_record = VehicleRepairRecord.objects.filter(id=self.kwargs['id']).first()
        print(repair_record)
        return repair_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class RepairRecordDeleteView(DeleteView):
    model = VehicleRepairRecord
    success_url = 'shop/vehicles_details.html'
    template_name = 'shop/vehicle_repair_record_delete_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        repair_record = VehicleRepairRecord.objects.filter(id=self.kwargs['id'])
        print(repair_record)
        return repair_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})


# ##################### DOT Record Related Views ########################3

class DotRecordCreateView(CreateView):
    form_class = shop.forms.vehicle_forms.DotRecordCreateForm
    # model = Vehicle
    template_name = 'shop/vehicle_dot_record_create_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def form_valid(self, form):
        form.instance.vehicle_id = self.kwargs.get('pk')
        print(self.kwargs.get('vid'))
        print(form.cleaned_data.get('dot_date'))

        # Grab the data from the service form
        date = form.cleaned_data.get('dot_inspection_date')
        miles = form.cleaned_data.get('dot_miles')

        # Get the Current Vehicle we are working on
        vehicle = Vehicle.objects.get(pk=self.kwargs.get('pk'))
        print(vehicle)
        # Update the dates for DOT stuff
        try:
            # Calculate the next DOT inspection date
            # dot_period = 12
            # print(f"Dot type is {type(dot_period)}")
            # if dot_period is None:
            #     print(f"I found dot_period is none {dot_period}")
            #     service_period = 12

            next_dot = date + timedelta(weeks=(52))

            print(next_dot)
            vehicle.next_dot = next_dot
            vehicle.last_dot = date

            # save to database
            vehicle.save()
        except Exception as e:
            print(e)

        return super(DotRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        print("I am displaying the Form Now!!!!")
        obj = Vehicle.objects.get(vehicle_id=self.kwargs['pk'])
        return obj


class DotRecordUpdateView(UpdateView):
    form_class = shop.forms.vehicle_forms.DotRecordUpdateForm
    template_name = 'shop/vehicle_dot_record_update_form.html'

    def form_valid(self, form, **kwargs):
        # Update the Trailer Object  so that if the status was changed the object will be changed
        vehicle = Vehicle.objects.get(vehicle_id=self.kwargs.get('pk'))
        vehicle.last_dot_status = form.cleaned_data['dot_passed_inspection']
        vehicle.save()

        return super(DotRecordUpdateView, self, ).form_valid(form)

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        dot_record = VehicleDotRecord.objects.filter(id=self.kwargs['id']).first()
        print(dot_record)
        return dot_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class DotRecordDeleteView(DeleteView):
    model = VehicleDotRecord
    success_url = 'shop/vehicles_details.html'
    template_name = 'shop/vehicle_dot_record_delete_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['vid'] = self.kwargs.get('vid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        dot_record = VehicleDotRecord.objects.filter(id=self.kwargs['id'])
        print(dot_record)
        return dot_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:detail_vehicles", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


######################################
# Inactive Related Views
######################################
class VehicleInactiveListView(ListView):
    model = Vehicle
    template_name = 'shop/vehicles_list.html'

    # context_object_name = 'vehicle_list'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(VehicleInactiveListView, self).get_context_data(**kwargs)
        # add extra field
        # *************Paginating the VEHICLE DATA ****************
        vehicles = Vehicle.objects.all().order_by(F('next_service').asc(nulls_last=True)).filter(vehicle_status=False)
        # Paginate the Service Records:
        paginated_vehicles = Paginator(vehicles, 9)
        page_number = self.request.GET.get('page')
        vehicles_page_obj = paginated_vehicles.get_page(page_number)

        # Add Paginated data to context
        context['vehicles_page_obj'] = vehicles_page_obj
        # ************* END Paginating the VEHICLE DATA ****************

        # ***************** END PAGINATION **************************
        context['vehicle_list'] = Vehicle.objects.all().order_by('next_service')
        print(context['vehicle_list'])
        context['today'] = datetime.date.today()
        context['today_20'] = datetime.date.today() + timedelta(14)

        return context


def AllServiceTasksListView(request):
    pass
    print("I am getting all things that need service")

    # Get the dates for today and 14 days into the future for service date calculations
    today = datetime.date.today()
    today_20 = datetime.date.today() + timedelta(14)

    # Get all the Objects that could require Servicing
    vehicles = Vehicle.objects.all().filter(next_service__lte=today_20) & Vehicle.objects.all().filter(
        vehicle_status__exact=True)
    trailers = Trailer.objects.all().filter(trailer_next_service__lte=today_20) & Trailer.objects.all().filter(
        trailer_status=True)
    equipments = Equipment.objects.all().filter(equipment_next_service__lte=today_20) & Equipment.objects.all().filter(
        equipment_status=True)
    print(equipments)
    # Add the properties that will be displayed in the results since they are to a specific model
    # We need to generalize them ex vehicle_short_name will be this_short_name
    for vehicle in vehicles:
        vehicle.this_service_date = vehicle.next_service
        vehicle.this_identifier = vehicle.vehicle_identifier
        vehicle.this_short_description = vehicle.vehicle_short_name
        vehicle.this_description = vehicle.vehicle_description
        vehicle.this_type = 'vehicle'

    for trailer in trailers:
        trailer.this_service_date = trailer.trailer_next_service
        trailer.this_identifier = trailer.trailer_identifier
        trailer.this_short_description = trailer.trailer_short_name
        trailer.this_description = trailer.trailer_description
        trailer.this_type = 'trailer'

    for equipment in equipments:
        equipment.this_service_date = equipment.equipment_next_service
        equipment.this_identifier = equipment.equipment_identifier
        equipment.this_short_description = equipment.equipment_short_name
        equipment.this_description = equipment.equipment_description
        equipment.this_type = 'equipment'

    # Combine all Objects into one List
    required_service = sorted(chain(vehicles, trailers, equipments), key=operator.attrgetter('this_service_date'),
                              reverse=False)
    print(required_service)
    # Set up The Pagination
    paginated_service_tasks = Paginator(required_service, 15)
    page_number = request.GET.get('page')
    service_tasks_page_obj = paginated_service_tasks.get_page(page_number)

    # End Pagination Set up

    # Add the paginated info to context dictionary
    context_mod = dict(required_service=service_tasks_page_obj)

    context_mod['trailer_nav'] = ''
    context_mod['vehicle_nav'] = ''
    context_mod['equipment_nav'] = ''
    context_mod['service_nav'] = 'active'
    context_mod['dot_nav'] = ''

    context_mod['today'] = today
    context_mod['today_20'] = today_20

    return render(request, "shop/required_service_tasks.html", context=context_mod)


def AllDotTasksListView(request):
    print("Entering DOT Task List")
    # Get the dates for today and 14 days into the future for service date calculations
    today = datetime.date.today()
    today_20 = datetime.date.today() + timedelta(14)

    # Get the Objects that will be evaluated for DOT Inspections
    vehicles = Vehicle.objects.all().filter(next_dot__lte=today_20)
    trailers = Trailer.objects.all().filter(trailer_next_dot__lte=today_20)

    # Add the properties that will be displayed in the results since they are to a specific model
    # We need to generalize them ex vehicle_short_name will be this_short_name
    for vehicle in vehicles:
        vehicle.this_next_dot = vehicle.next_dot
        vehicle.this_identifier = vehicle.vehicle_identifier
        vehicle.this_short_description = vehicle.vehicle_short_name
        vehicle.this_description = vehicle.vehicle_description
        vehicle.this_type = 'vehicle'

    for trailer in trailers:
        trailer.this_next_dot = trailer.trailer_next_dot
        trailer.this_identifier = trailer.trailer_identifier
        trailer.this_short_description = trailer.trailer_short_name
        trailer.this_description = trailer.trailer_description
        trailer.this_type = 'trailer'

    # Combine all Objects into one List
    required_dot_tasks = sorted(chain(vehicles, trailers), key=operator.attrgetter('this_next_dot'),
                                reverse=False)

    # Set up The Pagination
    paginated_dot_tasks = Paginator(required_dot_tasks, 15)
    page_number = request.GET.get('page')
    dot_tasks_page_obj = paginated_dot_tasks.get_page(page_number)

    # End Pagination Set up
    # Add the paginated info to context dictionary
    context_mod = dict(required_dot_tasks=dot_tasks_page_obj)

    context_mod['trailer_nav'] = ''
    context_mod['vehicle_nav'] = ''
    context_mod['equipment_nav'] = ''
    context_mod['service_nav'] = ''
    context_mod['dot_nav'] = 'active'

    context_mod['today'] = today
    context_mod['today_20'] = today_20

    return render(request, "shop/required_dot_tasks.html", context=context_mod)


class WeeklyCheckView(View):
    def get(self, request):
        # Query for the vehicles that are tracked weekly, Also Paginate at the same time with 15 items per page
        weekly_vehicles = Paginator(Vehicle.objects.all().filter(track_weekly_miles=True), 15)

        # Complete the Pagination process
        page_number = request.GET.get('page')
        weekly_tasks_page_obj = weekly_vehicles.get_page(page_number)

        #Create and Add the info to the Context

        #context_mod = dict(required_dot_tasks=dot_tasks_page_obj)
        context_mod = dict(weekly_tasks = weekly_tasks_page_obj)

        # Return to the view template
        return render(request, 'shop/required_weekly_service_tasks.html', context=context_mod)
        pass
