from django.contrib import admin
from .models import *
# Register your models here.


class network_type_admin(admin.ModelAdmin):
    list_display = ["id", "network_type"]
    list_per_page = 10
    list_editable = ["network_type"]
    search_fields = ["network_type"]


class interface_type_admin(admin.ModelAdmin):
    list_display = ["id", "interface_type"]
    list_per_page = 10
    list_editable = ["interface_type"]
    search_fields = ["interface_type"]


class room_admin(admin.ModelAdmin):
    list_display = ["id", "room"]
    list_per_page = 10
    list_editable = ["room"]
    search_fields = ["room"]


class protocal_admin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_per_page = 10
    list_editable = ["name"]
    search_fields = ["name"]


class group_dhcp_admin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_per_page = 10
    list_editable = ["name"]
    search_fields = ["name"]


class group_access_list_admin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_per_page = 10
    list_editable = ["name"]
    search_fields = ["name"]


class group_routing_admin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_per_page = 10
    list_editable = ["name"]
    search_fields = ["name"]


class vlan_admin(admin.ModelAdmin):
    list_display = ["id", "vlan_number", "name", "group_vlan"]
    list_per_page = 10
    list_editable = ["vlan_number", "name", "group_vlan"]
    list_filter = ["group_vlan"]
    search_fields = ["vlan_number", "name"]


class group_vlan_admin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_per_page = 10
    list_editable = ["name"]
    search_fields = ["name"]


class switch_port_mode_admin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_per_page = 10
    list_editable = ["name"]
    search_fields = ["name"]


class interface_device_admin(admin.ModelAdmin):
    list_display = ["id", "interface", "description",
                    "status", "network", "access"]
    list_per_page = 20
    list_editable = ["description", "status", "network", 'access']
    list_filter = ["network", 'access']
    search_fields = ["network", 'access']


class group_interface_admin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_per_page = 10
    list_editable = ["name"]
    search_fields = ["name"]


class intertrunk_admin(admin.ModelAdmin):
    list_display = ["id", "interface", "sub_interface",
                    "vlan", "address", "group_intertrunk"]
    list_per_page = 10
    list_editable = ["sub_interface", "vlan", "address", "group_intertrunk"]
    list_filter = ["interface", "group_intertrunk"]
    search_fields = ["interface", "group_intertrunk"]


class dhcp_admin(admin.ModelAdmin):
    list_display = ['id', 'excluded', 'dhcp_pool',  'network',
                    'default_router', 'dns_server', 'domain_name', 'group_dhcp']
    list_per_page = 10
    list_editable = ['group_dhcp']
    list_filter = ['group_dhcp']
    search_fields = ['group_dhcp']


class eigrp_admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'as_number',  'group_routing']
    list_per_page = 10
    list_editable = ['name', 'as_number',  'group_routing']
    list_filter = ['as_number', 'group_routing']
    search_fields = ['as_number', 'group_routing']


class profile_admin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10
    list_editable = ['name']
    list_filter = ['name']
    search_fields = ['name']


class username_admin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password']
    list_per_page = 10
    list_editable = ['username', 'password']
    search_fields = ['username']


class tudo_admin(admin.ModelAdmin):
    list_display = ['id', 'command', 'start', 'end', 'status']
    list_per_page = 20
    list_filter = ['start']
    search_fields = ['command']


class iot_admin(admin.ModelAdmin):
    list_display = ['id', 'mac', 'topic', 'subscribe',
                    'room', 'profile', 'network', 'lb_min', 'lb_max', 'lb_avg']
    list_per_page = 10
    list_editable = ['mac', 'topic', 'subscribe',
                     'room',  'profile',  'network', 'lb_min', 'lb_max', 'lb_avg']
    list_filter = ['room', 'lb_min', 'lb_max', 'lb_avg']
    search_fields = ['mac', 'topic']


class lb_stp_admin(admin.ModelAdmin):
    list_display = ['id', 'switch', 'root_bridge', 'command', 'time', 'date']
    list_per_page = 10
    list_filter = ['switch', 'date']
    search_fields = ['time', 'date']


class different_admin(admin.ModelAdmin):
    list_display = ['id', 'different', 'time', 'date']
    list_per_page = 10
    list_filter = ['date']


class count_admin(admin.ModelAdmin):
    list_display = ['id', 'switch', 'count']
    list_per_page = 10
# class topology_admin(admin.ModelAdmin):
#     list_display = ['id', 'topic']
#     list_per_page = 10
#     list_filter = ['topic']
#     search_fields = ['topic']


# class traffic_admin(admin.ModelAdmin):
#     list_display = ['id', 'topic', 'interface', 'packets']
#     list_per_page = 10
#     list_filter = ['topic']
#     search_fields = ['topic']


class network_admin(admin.ModelAdmin):
    list_display = ['id', 'hostname', 'pid', 'sn', 'network_type']
    list_per_page = 10
    list_editable = ['hostname', 'pid', 'sn', 'network_type']
    list_filter = ['network_type']
    search_fields = ['hostname']


admin.site.register(network_type_table, network_type_admin)
admin.site.register(interface_type_table, interface_type_admin)
admin.site.register(room_table, room_admin)
admin.site.register(protocal_table, protocal_admin)
admin.site.register(tudo_table, tudo_admin)
# Group
admin.site.register(group_dhcp_table, group_dhcp_admin)
admin.site.register(group_acl_table, group_access_list_admin)
admin.site.register(group_routing_table, group_routing_admin)
admin.site.register(group_vlan_table, group_vlan_admin)
admin.site.register(group_interface_table, group_interface_admin)
# Switch and Router
admin.site.register(vlan_table, vlan_admin)
admin.site.register(switchport_mode_table, switch_port_mode_admin)
admin.site.register(interface_table, interface_device_admin)
admin.site.register(intertrunk_table, intertrunk_admin)
admin.site.register(dhcp_table, dhcp_admin)
admin.site.register(eigrp_table, eigrp_admin)
# Profile
admin.site.register(profile_table, profile_admin)
admin.site.register(username_table, username_admin)
admin.site.register(iot_table, iot_admin)
# admin.site.register(topology_table, topology_admin)
# admin.site.register(traffic_table, traffic_admin)
admin.site.register(network_table, network_admin)
admin.site.register(load_balance_stp_table, lb_stp_admin)
admin.site.register(different_table, different_admin)
admin.site.register(count_table, count_admin)