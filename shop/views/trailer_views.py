import datetime
from datetime import timedelta

from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q, F

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

import shop.models
# from shop.models import Vehicle, Trailer, Equipment, \
#    VehicleServiceRecord, VehicleRepairRecord, VehicleDotRecord
from shop.models import *
from shop.forms.trailer_forms import *


# Create your views here.
######################################
# Trailer Related Views
######################################

class TrailerListView(ListView):
    model = Trailer
    template_name = 'shop/trailer_list.html'
    queryset = Trailer.objects.all().order_by(F('trailer_next_service').asc(nulls_last=True)).filter(
        trailer_status=True)

    # context_object_name = 'vehicle_list'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(TrailerListView, self).get_context_data(**kwargs)
        # add extra field

        # *************Paginating the Trailer DATA ****************
        trailers = Trailer.objects.all().order_by(F('trailer_next_service').asc(nulls_last=True)).filter(
            trailer_status=True)
        # Paginate the Service Records:
        paginated_trailers = Paginator(trailers, 9)
        page_number = self.request.GET.get('page')
        trailers_page_obj = paginated_trailers.get_page(page_number)
        # Add Paginated data to context
        context['trailers_page_obj'] = trailers_page_obj
        print(f"The TrailersList Pagination Object is {trailers_page_obj}")
        # ************* END Paginating the Trailer DATA ****************

        # ***************** END PAGINATION **************************
        # Set the Active Tab
        context['vehicle_nav'] = ''
        context['trailer_nav'] = 'active'
        context['equipment_nav'] = ''
        context['service_nav'] = ''
        context['dot_nav'] = ''

        context['trailers_list'] = Trailer.objects.all().order_by('trailer_next_service')
        print(context['trailers_list'])
        context['today'] = datetime.date.today()
        context['today_20'] = datetime.date.today() + timedelta(14)

        return context


# This Main be Absolete as all Records Views are handled throught the Vehicle, Trailer, Equipment Views

class TrailerCreateView(CreateView):
    form_class = CreateTrailerForm
    # model = Vehicle
    template_name = 'shop/trailer_create_form.html'

    # fields = ['vehicle_license', 'vehicle_vin', 'vehicle_identifier',
    #         'vehicle_department', 'vehicle_short_name', 'vehicle_description']

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailers_list")
        # return reverse("shop:list_vehicles")


class TrailerDetailsView(DetailView):
    model = Trailer
    template_name = 'shop/trailer_details.html'

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(TrailerDetailsView, self).get_context_data(**kwargs)
        queryset = self.get_queryset()

        # *************Paginating the VEHICLE DATA ****************
        trailers = queryset.order_by(F('trailer_next_service').asc(nulls_last=True))
        test = queryset.order_by(F('trailer_next_service'))

        print(f"The test is: {test}")
        # Paginate the Service Records:
        paginated_trailers = Paginator(trailers, 9)
        page_number = self.request.GET.get('page')
        trailers_page_obj = paginated_trailers.get_page(page_number)

        # Add Paginated data to context
        context['vehicles_page_obj'] = trailers_page_obj

        print("Getting Trailer Service Records")
        # Get the Service Records
        service_records = TrailerServiceRecord.objects.filter(trailer=self.kwargs['pk']).select_related(
            'trailer').order_by('trailer_service_date').reverse()
        print(f"The trailer service records are: {service_records}")
        # Paginate the Service Records:
        paginated_service_records = Paginator(service_records, 7)
        page_number = self.request.GET.get('page')
        service_records_page_obj = paginated_service_records.get_page(page_number)
        # Add the Service Records to the context
        context["service_records"] = service_records
        context['service_records_page_obj'] = service_records_page_obj

        # Get the Repair Records

        repair_records = TrailerRepairRecord.objects.filter(trailer=self.kwargs['pk']).select_related(
            'trailer').order_by('trailer_repair_date').reverse()
        # Paginate the Service Records:
        paginated_repair_records = Paginator(repair_records, 7)
        repair_page_number = self.request.GET.get('page')
        repair_records_page_obj = paginated_repair_records.get_page(repair_page_number)
        # Add the Service Records to the context
        context["repair_records"] = repair_records
        context['repair_records_page_obj'] = repair_records_page_obj

        # Get the DOT Inspection Records
        dot_records = TrailerDotRecord.objects.filter(trailer=self.kwargs['pk']).select_related(
            'trailer').order_by('trailer_dot_inspection_date').reverse()
        # Paginate the Service Records:
        print(f"The Dot Records\n{dot_records}")
        paginated_dot_records = Paginator(dot_records, 7)
        dot_page_number = self.request.GET.get('page')
        dot_records_page_obj = paginated_dot_records.get_page(dot_page_number)
        # Add the Service Records to the context

        context["dot_records"] = dot_records
        context['dot_records_page_obj'] = dot_records_page_obj

        # Set the Active Tab
        context['vehicle_nav'] = ''
        context['trailer_nav'] = 'active'
        context['equipment_nav'] = ''
        context['service_nav'] = ''
        context['dot_nav'] = ''

        return context


class TrailerUpdate1(UpdateView):
    form_class = UpdateTrailerForm1
    template_name = 'shop/trailer_update_form.html'
    pk_url_kwarg = Trailer.trailer_id

    # success_url = reverse_lazy('shop:detail_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Trailer.objects.get(trailer_id=self.kwargs['pk'])
        return obj


class TrailerUpdate2(UpdateView):
    form_class = UpdateTrailerForm2
    template_name = 'shop/trailer_update_form.html'
    pk_url_kwarg = Trailer.trailer_id

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Trailer.objects.get(trailer_id=self.kwargs['pk'])
        return obj


class TrailerUpdate3(UpdateView):
    form_class = UpdateTrailerForm3
    template_name = 'shop/trailer_update_form.html'

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Trailer.objects.get(trailer_id=self.kwargs['pk'])
        return obj


class TrailerUpdate4(UpdateView):
    form_class = UpdateTrailerForm4
    template_name = 'shop/trailer_update_form.html'

    # success_url = reverse_lazy('shop:list_vehicles')

    def get_success_url(self, *args, **kwargs):
        print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Trailer.objects.get(trailer_id=self.kwargs['pk'])
        return obj


class TrailerSearchListView(ListView):
    model = Trailer
    template_name = 'shop/trailer_list.html'

    def get_queryset(self):
        print('Entering Trailer get_queryset')
        # Get the search parameters
        qsearch = self.request.GET.get('q')
        dsearch = self.request.GET.get('department')
        status = self.request.GET.get('item_status')

        # Set the dsearch to blank if a None is returned since query does not handle None
        if dsearch is None:
            dsearch = ""

        # Print out the search parameters for debugging
        print(f"Q is: {qsearch}\nDepartment is: {dsearch}\nStatus is: {status}")

        # Perform the base query to select either active or inactive vehicles
        if status == 'Active':
            print(f"Searching for {status} Trailers")
            queryset_status = Trailer.objects.all().order_by(F('trailer_next_service').asc(nulls_last=True)).filter(
                trailer_status=True)
        else:
            print(f"Searching for {status} Trailers")
            queryset_status = Trailer.objects.all().order_by(F('trailer_short_name').asc(nulls_last=True)).filter(
                trailer_status=False)

        # Perform the enhanced Query for when other search items selected
        if dsearch and not qsearch:
            print(f"Hello I am in department only: {dsearch}")
            queryset = queryset_status.filter(trailer_department=dsearch).order_by('trailer_next_service')
            print(queryset)
            return queryset

        elif qsearch and not dsearch:
            print("Getting result for text search only")
            q_short_des = Q(trailer_short_name__icontains=qsearch)
            # q_assigned = Q(assigned_employee__icontains=qsearch)
            q_des = Q(trailer_description__icontains=qsearch)
            q_id = Q(trailer_identifier__icontains=qsearch)
            q_license = Q(trailer_license__icontains=qsearch)
            queryset = queryset_status.filter(Q(q_short_des | q_des | q_id) | q_license)
            return queryset

        elif qsearch and dsearch:
            print('Getting search for Both Q and Department')
            queryset = queryset_status.filter(
                Q(Q(trailer_short_name__icontains=qsearch) |
                  Q(trailer_description__icontains=qsearch) |
                  Q(trailer_license__icontains=qsearch)) &
                Q(trailer_department=dsearch))
            return queryset
        else:
            print("There was no q")
            queryset = queryset_status.order_by('trailer_next_service')

        return queryset

    # override context data
    def get_context_data(self, *args, **kwargs):
        context_mod = super(TrailerSearchListView, self).get_context_data(**kwargs)

        # Get the Query Set from the get_query set function
        queryset = self.get_queryset()

        # *************Paginating the Trailer DATA ****************
        trailers = queryset.order_by(F('trailer_identifier').asc(nulls_last=True))

        # Paginate the Service Records:
        paginated_trailers = Paginator(trailers, 9)
        page_number = self.request.GET.get('page')
        trailers_page_obj = paginated_trailers.get_page(page_number)
        # Add Paginated data to context
        context_mod['trailers_page_obj'] = trailers_page_obj
        print(f"The TrailersList Pagination Object is {trailers_page_obj}")
        # ************* END Paginating the Trailer DATA ****************

        # Add Search Releated Items to Context
        context_mod['selected_item_status'] = self.request.GET.get('item_status')
        context_mod['selected_department'] = self.request.GET.get("department")
        context_mod['search_text'] = self.request.GET.get('q')
        context_mod['selected_q'] = self.request.GET.get("q")

        context_mod['trailer_nav'] = 'active'
        context_mod['vehicle_nav'] = ''
        context_mod['equipment_nav'] = ''
        context_mod['service_nav'] = ''
        context_mod['dot_nav'] = ''

        # context['vehicle_list'] = queryset
        context_mod['today'] = datetime.date.today()
        context_mod['today_20'] = datetime.date.today() + timedelta(14)
        print(f"The Trailer Search Context is: {context_mod}")
        return context_mod


class TrailerServiceRecordCreateView(CreateView):
    form_class = ServiceRecordCreateForm
    # model = Vehicle
    template_name = 'shop/trailer_service_record_create_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def form_valid(self, form):
        form.instance.trailer_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(form.cleaned_data.get('trailer_service_date'))

        # Grab the data from the service form
        date = form.cleaned_data.get('trailer_service_date')
        print(f"The service date for trailer {date}")
        # Get the Current trailer we are working on
        trailer = Trailer.objects.get(pk=self.kwargs.get('pk'))

        try:
            # Calculate the next service date
            service_period = trailer.trailer_service_period
            print(f"Service type is {type(service_period)}")
            if service_period is None:
                print(f"I found service_period is none {service_period}")
                service_period = 6
                trailer.trailer_service_period = service_period
            next_service = date + timedelta(weeks=(service_period * 4))

            print(next_service)
            trailer.trailer_next_service = next_service
            trailer.trailer_last_service = date

            # save to database
            trailer.save()
        except Exception as e:
            print(f"The Trailer Date Exception is: {e}")

        # print(next_service, type(next_service))

        # Update all the service info

        return super(TrailerServiceRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Trailer.objects.get(trailer_id=self.kwargs['pk'])
        return obj


class TrailerServiceRecordDeleteView(DeleteView):
    model = TrailerServiceRecord
    success_url = 'shop/trailer_details.html'
    template_name = 'shop/trailer_service_record_delete_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        service_record = TrailerServiceRecord.objects.filter(id=self.kwargs['id'])
        print(service_record)
        return service_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class TrailerServiceRecordUpdateView(UpdateView):
    form_class = TrailerServiceRecordUpdateForm
    template_name = 'shop/trailer_service_record_update_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        service_record = TrailerServiceRecord.objects.filter(id=self.kwargs['id']).first()
        print(service_record)
        return service_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


# #####################Repair Record Related Views ########################3

class TrailerRepairRecordCreateView(CreateView):
    form_class = TrailerRepairRecordCreateForm
    # model = Vehicle
    template_name = 'shop/trailer_repair_record_create_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def form_valid(self, form):
        form.instance.trailer_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(form.cleaned_data.get('trailer_repair_date'))

        return super(TrailerRepairRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Trailer.objects.get(trailer_id=self.kwargs['pk'])
        return obj


class TrailerRepairRecordUpdateView(UpdateView):
    form_class = TrailerRepairRecordUpdateForm
    template_name = 'shop/trailer_repair_record_update_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        repair_record = TrailerRepairRecord.objects.filter(id=self.kwargs['id']).first()
        print(repair_record)
        return repair_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class TrailerRepairRecordDeleteView(DeleteView):
    model = TrailerServiceRecord
    success_url = 'shop/trailer_details.html'
    template_name = 'shop/trailer_repair_record_delete_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        repair_record = TrailerRepairRecord.objects.filter(id=self.kwargs['id'])
        print(repair_record)
        return repair_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


# ##################### DOT Record Related Views ########################3

class TrailerDotRecordCreateView(CreateView):
    form_class = TrailerDotRecordCreateForm
    template_name = 'shop/trailer_dot_record_create_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def form_valid(self, form):
        form.instance.trailer_id = self.kwargs.get('pk')
        print(self.kwargs.get('pk'))
        print(f"the Cleaned data is{form.cleaned_data}")

        # Grab the data from the service form
        date = form.cleaned_data.get('trailer_dot_inspection_date')
        print(f"The Trailer Inspection Date is: {date}")

        # Get the Current Vehicle we are working on
        trailer = Trailer.objects.get(pk=self.kwargs.get('pk'))
        print(f"The Trailer is: {trailer}")
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
            trailer.trailer_next_dot = next_dot
            trailer.trailer_last_dot = date

            # save to database
            trailer.save()
        except Exception as e:
            print(e)

        return super(TrailerDotRecordCreateView, self, ).form_valid(form)

    # success_url = reverse_lazy('shop:list_vehicles')
    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")

    def get_object(self, queryset=None):
        # get the existing object or created a new one
        obj = Trailer.objects.get(trailer_id=self.kwargs['pk'])
        return obj


class TrailerDotRecordUpdateView(UpdateView):
    form_class = TrailerDotRecordUpdateForm
    template_name = 'shop/trailer_dot_record_update_form.html'

    def form_valid(self, form, **kwargs):
        # Update the Trailer Object  so that if the status was changed the object will be changed
        trailer = Trailer.objects.get(trailer_id=self.kwargs.get('pk'))
        trailer.trailer_last_dot_status = form.cleaned_data['trailer_dot_passed_inspection']
        trailer.save()

        return super(TrailerDotRecordUpdateView, self, ).form_valid(form)

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        dot_record = TrailerDotRecord.objects.filter(id=self.kwargs['id']).first()
        print(dot_record)
        return dot_record

    def get_success_url(self, *args, **kwargs):
        # print(self.kwargs)
        # return reverse_lazy("shop:detail_vehicles", kwargs={'pk': 1})
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})
        # return reverse("shop:list_vehicles")


class TrailerDotRecordDeleteView(DeleteView):
    model = shop.models.TrailerDotRecord
    success_url = 'shop/trailer_details.html'
    template_name = 'shop/trailer_dot_record_delete_form.html'

    def get_context_data(self, **kwargs):
        context_mod = super().get_context_data(**kwargs)
        context_mod['tid'] = self.kwargs.get('tid')
        return context_mod

    def get_object(self, queryset=None, **kwargs):
        # get the existing object or created a new one
        print(kwargs)
        dot_record = TrailerDotRecord.objects.filter(id=self.kwargs['id'])
        print(dot_record)
        return dot_record

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy("shop:trailer_details", kwargs={'pk': self.kwargs['pk']})

######################################
# Trailer Related Views
######################################
