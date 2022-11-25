from django.urls import path

import shop.views.vehicle_views
from shop.views.vehicle_views import *
from shop.views.trailer_views import *
from shop.views.equipment_views import *

app_name = 'shop'

urlpatterns = [
    #    path('home/', shop.views.vehicle_views.home_page, name='home'),
    path('', AllServiceTasksListView, name='all_service_tasks'),

    path('vehicles_list', ListVehiclesView.as_view(), name='vehicles_list'),
    path('vehicles_details/<int:pk>', VehicleDetailsView.as_view(), name='detail_vehicles'),
    path('vehicile_create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicile_update1/<int:pk>', VehicleUpdate1.as_view(), name='vehicle_update1'),
    path('vehicile_update2/<int:pk>', VehicleUpdate2.as_view(), name='vehicle_update2'),
    path('vehicile_update3/<int:pk>', VehicleUpdate3.as_view(), name='vehicle_update3'),
    path('vehicile_update4/<int:pk>', VehicleUpdate4.as_view(), name='vehicle_update4'),

    # Vehicle Service Records

    path('service_record_create/<int:pk> <int:vid>', ServiceRecordCreateView.as_view(),
         name='service_record_create'),
    path('service_record_delete/<int:id> <int:pk> <int:vid>', ServiceRecordDeleteView.as_view(),
         name='service_record_delete'),
    path('service_record_update/<int:id> <int:pk> <int:vid>', ServiceRecordUpdateView.as_view(),
         name='service_record_update'),

    # Vehicle Repair Records

    path('repair_record_create/<int:pk> <int:vid>', RepairRecordCreateView.as_view(),
         name='repair_record_create'),
    path('repair_record_delete/<int:id> <int:pk> <int:vid>', RepairRecordDeleteView.as_view(),
         name='repair_record_delete'),
    path('repair_record_update/<int:id> <int:pk> <int:vid>', RepairRecordUpdateView.as_view(),
         name='repair_record_update'),

    # Vehicle Dot Records

    path('dot_record_create/<int:pk> <int:vid>', DotRecordCreateView.as_view(),
         name='dot_record_create'),
    path('dot_record_update/<int:id> <int:pk> <int:vid>', DotRecordUpdateView.as_view(),
         name='dot_record_update'),
    path('dot_record_delete/<int:id> <int:pk> <int:vid>', DotRecordDeleteView.as_view(),
         name='dot_record_delete'),
    path('search_vehicles', SearchListVehiclesView.as_view(), name='search_vehicles'),

    ##### Start Trailer URL'S

    path('trailer_create/', TrailerCreateView.as_view(), name='trailer_create'),
    path('trailers_list/', TrailerListView.as_view(), name='trailers_list'),
    path('search_trailers', TrailerSearchListView.as_view(), name='search_trailers'),
    path('trailer_details/<int:pk>', TrailerDetailsView.as_view(), name='trailer_details'),

    path('trailer_update1/<int:pk>', TrailerUpdate1.as_view(), name='trailer_update1'),
    path('trailer_update2/<int:pk>', TrailerUpdate2.as_view(), name='trailer_update2'),
    path('trailer_update3/<int:pk>', TrailerUpdate3.as_view(), name='trailer_update3'),
    path('trailer_update4/<int:pk>', TrailerUpdate4.as_view(), name='trailer_update4'),

    path('trailer_service_record_create/<int:pk> <int:tid>', TrailerServiceRecordCreateView.as_view(),
         name='trailer_service_record_create'),
    path('trailer_service_record_delete/<int:id> <int:pk> <int:tid>', TrailerServiceRecordDeleteView.as_view(),
         name='trailer_service_record_delete'),
    path('trailer_service_record_update/<int:id> <int:pk> <int:tid>', TrailerServiceRecordUpdateView.as_view(),
         name='trailer_service_record_update'),

    path('trailer_repair_record_create/<int:pk> <int:tid>', TrailerRepairRecordCreateView.as_view(),
         name='trailer_repair_record_create'),
    path('trailer_repair_record_delete/<int:id> <int:pk> <int:tid>', TrailerRepairRecordDeleteView.as_view(),
         name='trailer_repair_record_delete'),
    path('trailer_repair_record_update/<int:id> <int:pk> <int:tid>', TrailerRepairRecordUpdateView.as_view(),
         name='trailer_repair_record_update'),

    path('trailer_dot_record_create/<int:pk> <int:tid>', TrailerDotRecordCreateView.as_view(),
         name='trailer_dot_record_create'),
    path('trailer_dot_record_update/<int:id> <int:pk> <int:tid>', TrailerDotRecordUpdateView.as_view(),
         name='trailer_dot_record_update'),
    path('trailer_dot_record_delete/<int:id> <int:pk> <int:tid>', TrailerDotRecordDeleteView.as_view(),
         name='trailer_dot_record_delete'),

    #### Start of Equipment URL's

    path('equipment_create/', EquipmentCreateView.as_view(), name='equipment_create'),
    path('equipment_list/', EquipmentListView.as_view(), name='equipment_list'),
    path('search_equipment', EquipmentSearchListView.as_view(), name='search_equipment'),
    path('equipment_details/<int:pk>', EquipmentDetailsView.as_view(), name='equipment_details'),

    path('eqiupment_update1/<int:pk>', EquipmentUpdate1.as_view(), name='equipment_update1'),
    path('equipment_update2/<int:pk>', EquipmentUpdate2.as_view(), name='equipment_update2'),
    path('equipment_update3/<int:pk>', EquipmentUpdate3.as_view(), name='equipment_update3'),
    # path('equipment_update4/<int:pk>', EquipmentUpdate4.as_view(), name='equipment_update4'),

    path('equipment_service_record_create/<int:pk>', EquipmentServiceRecordCreateView.as_view(),
         name='equipment_service_record_create'),
    path('equipment_sservice_record_delete/<int:id> <int:pk>', EquipmentServiceRecordDeleteView.as_view(),
         name='equipment_service_record_delete'),
    path('equipment_service_record_update/<int:id> <int:pk>', EquipmentServiceRecordUpdateView.as_view(),
         name='equipment_service_record_update'),

    path('equipment_repair_record_create/<int:pk>', EquipmentRepairRecordCreateView.as_view(),
         name='equipment_repair_record_create'),
    path('equipment_repair_record_delete/<int:id> <int:pk>', EquipmentRepairRecordDeleteView.as_view(),
         name='equipment_repair_record_delete'),
    path('equipment_repair_record_update/<int:id> <int:pk>', EquipmentRepairRecordUpdateView.as_view(),
         name='equipment_repair_record_update'),

    #  Service Tasks Menu Item
    path('all_service_tasks/', AllServiceTasksListView, name='all_service_tasks'),

]

#    path('xxx/', ListVehiclesView.as_view(), name='list_vehicles'),
