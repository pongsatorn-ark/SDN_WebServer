"""DevNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from python.django.DevNet.network.controller.user import register
from django.urls import path
from django.contrib import admin
from network.controller import iot_device, user, monitor, network_device, profile, deploy_config, config, router_config
# from network import mqtt

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', mqtt.data_mqtt, name='data_mqtt'),
    path('', monitor.dashboard, name='dashboard'),
    # register
    path('register/', user.register, name='register'),
    path('register/add/', user.adduser, name='adduser'),
    # Begin Iot Device
    path('iot_device/', iot_device.iot_list, name='iot_list'),
    path('iot_device/iot_add/', iot_device.iot_add, name='iot_add'),
    path('iot_device/delete/<int:id>',
         iot_device.iot_delete, name="iot_delete"),
    path('iot_update/<int:pk>', iot_device.iot_update, name="iot_update"),
    # Begin Deploy Configuration
    path('config/<int:id>,<int:profile_id>,<int:network_type_id>',
         iot_device.config, name="config"),
    # path('deploy_config/<int:id>',
    #      deploy_config.deploy_config, name="deploy_config"),
    # Begin Network Device
    path('network_device/', network_device.network_list, name='network_list'),
    path('network_device/new', network_device.network_new, name='network_new'),
    path('network_device/save/', network_device.network_save, name="network_save"),
    path('network_device/delete/<int:id>',
         network_device.network_delete, name='network_device'),
    path('network_generate/<int:pk>',
         network_device.network_generate, name="network_generate"),
    path('network_update/<int:pk>',
         network_device.network_update, name="network_update"),
    # Begin Profile
    path('profile/', profile.profile_list, name="profile_list"),
    path('profile/new/', profile.profile_new, name="profile_name"),
    # path('profile/save/', profile.profile_save, name="profile_save"),
    path('profile/delete/<int:id>', profile.profile_delete, name="profile_delete"),
    path('profile/<int:pk>', profile.profile_update, name="profile_update"),
    # path('profile/update/<int:id>', profile.profile_update_save,
    #      name="profile_update_save"),
    # Config
    # path('vlan/')
    # Configuration
    # DHCP
    path('group_dhcp/', config.group_dhcp),
    path('group_dhcp/save/', config.group_dhcp_save),
    path('group_dhcp/edit/<int:pk>', config.group_dhcp_edit),
    path('group_dhcp/delete/<int:pk>', config.group_dhcp_delete),
    # Routing
    path('group_routing/', config.group_routing),
    path('group_routing/save/', config.group_routing_save),
    path('group_routing/edit/<int:pk>', config.group_routing_edit),
    path('group_routing/delete/<int:pk>', config.group_routing_delete),
    # access_list
    path('group_access_list/', config.group_access_list),
    path('group_access_list/save/', config.group_access_list_save),
    path('group_access_list/edit/<int:pk>', config.group_access_list_edit),
    path('group_access_list/delete/<int:pk>', config.group_access_list_delete),
    # sub_interface
    path('group_sub_interface/', config.group_sub_interface),
    path('group_sub_interface/save/', config.group_sub_interface_save),
    path('group_sub_interface/edit/<int:pk>', config.group_sub_interface_edit),
    path('group_sub_interface/delete/<int:pk>',
         config.group_sub_interface_delete),
    # vlan
    path('group_vlan/', config.group_vlan),
    path('group_vlan/save/', config.group_vlan_save),
    path('group_vlan/edit/<int:pk>', config.group_vlan_edit),
    path('group_vlan/delete/<int:pk>', config.group_vlan_delete),
    # switchport
    path('group_switch_port/', config.group_switch_port),
    path('group_switch_port/save/', config.group_switch_port_save),
    path('group_switch_port/edit/<int:pk>', config.group_switch_port_edit),
    path('group_switch_port/delete/<int:pk>', config.group_switch_port_delete),
    # port channel
    path('group_port_channel/', config.group_port_channel),
    path('group_port_channel/save/', config.group_port_channel_save),
    path('group_port_channel/edit/<int:pk>', config.group_port_channel_edit),
    path('group_port_channel/delete/<int:pk>',
         config.group_port_channel_delete),
    # DHCP
    path('router/dhcp', router_config.dhcp_list, name="dhcp-list"),
    path('router/dhcp/add', router_config.dhcp_create, name="dhcp-create"),
    path('router/dhcp/edit/<int:id>', router_config.dhcp_edit, name="dhcp-edit"),
    path('router/dhcp/delete/<int:id>',
         router_config.dhcp_delete, name="dhcp-delete"),
    # HSRP
    path('router/hsrp', router_config.hsrp_list, name="hsrp-list"),
    path('router/hsrp/add', router_config.hsrp_create, name="hsrp-create"),
    path('router/hsrp/edit/<int:id>', router_config.hsrp_edit, name="hsrp-edit"),
    path('router/hsrp/delete/<int:id>',
         router_config.hsrp_delete, name="hsrp-delete"),
    # Sub Interface
    path('router/sub_interface', router_config.sub_interface_list,
         name="sub_interface-list"),
    path('router/sub_interface/add', router_config.sub_interface_create,
         name="sub_interface-create"),
    path('router/sub_interface/edit/<int:id>',
         router_config.sub_interface_edit, name="sub_interface-edit"),
    path('router/sub_interface/delete/<int:id>',
         router_config.sub_interface_delete, name="sub_interface-delete"),
    # Static Route
    path('router/static_route', router_config.static_list, name="static-list"),
    path('router/static_route/add',
         router_config.static_create, name="static-create"),
    path('router/static_route/edit/<int:id>',
         router_config.static_edit, name="static-edit"),
    path('router/static_route/delete/<int:id>',
         router_config.static_delete, name="static-delete"),
    # EIGRP Route
    path('router/eigrp', router_config.eigrp_list, name="eigrp-list"),
    path('router/eigrp/add',
         router_config.eigrp_create, name="eigrp-create"),
    path('router/eigrp/edit/<int:id>',
         router_config.eigrp_edit, name="eigrp-edit"),
    path('router/eigrp/delete/<int:id>',
         router_config.eigrp_delete, name="eigrp-delete"),
]
