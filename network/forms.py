from typing import ClassVar
from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import *


class forms_iot(forms.ModelForm):
    class Meta:
        model = iot_table
        fields = ['id', 'mac', 'topic', 'room',
                  'profile', 'network', 'subscribe']
        labels = {
            'id': 'ID',
            'mac': 'MAC Address',
            'topic': 'Topic',
            'subscribe': 'Subscribe',
            'room': 'Select Room',
            'profile': 'Select Profile',
            'network': 'Select Network Device',
        }

    def __init__(self, *args, **kwargs):
        super(forms_iot, self).__init__(*args, **kwargs)
        self.fields['room'].empty_label = "-- Select Room --"
        self.fields['profile'].empty_label = "-- Select Profile --"
        self.fields['network'].empty_label = "-- Select Network Device --"


class forms_network(forms.ModelForm):
    class Meta:
        model = network_table
        fields = ['id', 'hostname', 'pid', 'sn',
                  'interface_type', 'network_type']
        labels = {
            'hostname': 'Hostname',
            'pid': 'Product Identification (PID)',
            'sn': 'Serial number (SN)',
            'interface_type': 'Select Interface Type',
            'network_type': 'Select Network Type',
        }

    def __init__(self, *args, **kwargs):
        super(forms_network, self).__init__(*args, **kwargs)
        self.fields['interface_type'].empty_label = "-- Select Interface Type --"
        self.fields['network_type'].empty_label = "-- Select Network Type --"


class froms_profile(forms.ModelForm):
    class Meta:
        model = profile_table
        fields = '__all__'
        labels = {
            'id': 'id',
            'name': 'Profile Name',
            'domain_lookup': 'Disable DNS Lookup',
            'service_pwd': 'Encrypt Text Password',
            'domain_name': 'Domain Name',
            'username': 'username',
            'console': 'Secure Console',
            'vty': 'Secure VTY',
            'ssh': 'Secure Shell (SSH)',
            'neighbor': 'Cisco Discovery Protocol (CDP)',
            'key': 'Crypto Key Generate',
            'default_gateway': 'Default Gateway',
            'group_vlan': 'Group VLAN',
            'group_switchport': 'Group SwitchPort',
            'group_portchannel': 'Group PortChannel',
            'group_routing': 'Group Routing',
            'group_acl': 'Group ACL',
            'group_intertrunk': 'Group Sub-Innterface',
            'group_dhcp': 'Group DHCP',
        }

    def __init__(self, *args, **kwargs):
        super(froms_profile, self).__init__(*args, **kwargs)
        self.fields['group_vlan'].empty_label = "-- Group VLAN --"
        self.fields['group_switchport'].empty_label = "-- Group SwitchPort --"
        self.fields['group_portchannel'].empty_label = "-- Group PortChannel --"
        self.fields['group_routing'].empty_label = "-- Group Routing --"
        self.fields['group_acl'].empty_label = "-- Group ACL --"
        self.fields['group_intertrunk'].empty_label = "-- Group Sub-Innterface --"
        self.fields['group_dhcp'].empty_label = "-- Group DHCP --"
        self.fields['username'].empty_label = "-- Select Username --"


class forms_username(forms.ModelForm):
    class Meta:
        model = username_table
        fields = '__all__'
        labels = {
            'username': 'username',
            'password': 'password',
        }


class forms_group_dhcp(forms.ModelForm):
    class Meta:
        model = group_dhcp_table
        fields = '__all__'
        labels = {
            'name': 'Group Name'
        }


class forms_group_routing(forms.ModelForm):
    class Meta:
        model = group_routing_table
        fields = '__all__'
        labels = {
            'name': 'Group Name'
        }


class forms_group_access_list(forms.ModelForm):
    class Meta:
        model = group_acl_table
        fields = '__all__'
        labels = {
            'name': 'Group Name'
        }


class forms_group_sub_interface(forms.ModelForm):
    class Meta:
        model = group_intertrunk_table
        fields = '__all__'
        labels = {
            'name': 'Group Name'
        }


class forms_group_vlan_table(forms.ModelForm):
    class Meta:
        model = group_vlan_table
        fields = '__all__'
        labels = {
            'name': 'Group Name'
        }


class forms_group_switchport_table(forms.ModelForm):
    class Meta:
        model = group_switchport_table
        fields = '__all__'
        labels = {
            'name': 'Group Name'
        }


class forms_group_portchannel_table(forms.ModelForm):
    class Meta:
        model = group_portchannel_table
        fields = '__all__'
        labels = {
            'name': 'Group Name'
        }


class forms_network_type(forms.ModelForm):
    class Meta:
        model = network_type_table
        fields = '__all__'
        lables = {
            'network_type': 'Network Type',
        }


class forms_dhcp(forms.ModelForm):
    class Meta:
        model = dhcp_table
        fields = '__all__'
        labels = {
            'excluded': 'Excluded-Address ',
            'dhcp_pool': 'DHCP POOL Name',
            'interface_helper': 'Interface Helper',
            'helper_address': 'Address',
            'network': 'DHCP Network',
            'default_router': 'DHCP Gateway',
            'dns_server': 'DHCP DNS',
            'domain_name': 'DHCP Domain Name',
            'group_dhcp': 'DHCP Group',
        }

    def __init__(self, * args, **kwargs):
        super(forms_dhcp, self).__init__(*args, **kwargs)
        self.fields['interface_helper'].empty_label = "-- Interface helper --"
        self.fields['group_dhcp'].empty_label = "-- Group DHCP --"


class forms_hsrp(forms.ModelForm):
    class Meta:
        model = hsrp_table
        fields = '__all__'
        labels = {
            'interface': 'Interfaces',
            'standby_number': 'Standby Number',
            'vip': 'Visual IP',
            'priority': 'Priority',
        }

    def __init__(self, * args, **kwargs):
        super(forms_hsrp, self).__init__(*args, **kwargs)
        self.fields['interface'].empty_label = "-- Select interface --"


class forms_sub_interface(forms.ModelForm):
    class Meta:
        model = intertrunk_table
        fields = '__all__'
        labels = {
            'interface': 'Interfaces',
            'sub_interface': 'Sub Interface Number',
            'vlan': 'VLAN Number',
            'address': 'Address',
            'group_intertrunk': 'Group',
        }

    def __init__(self, * args, **kwargs):
        super(forms_sub_interface, self).__init__(*args, **kwargs)
        self.fields['interface'].empty_label = "-- Select interface --"
        self.fields['group_intertrunk'].empty_label = "-- Select Group --"


class forms_static(forms.ModelForm):
    class Meta:
        model = static_route_table
        fields = '__all__'
        labels = {
            'name': 'Name Route',
            'network_netmask_route': 'Allow Address/Netmask/Gateway',
            'group_routing': 'Group',
        }

    def __init__(self, * args, **kwargs):
        super(forms_static, self).__init__(*args, **kwargs)
        self.fields['group_routing'].empty_label = "-- Select Group --"


class forms_eigrp_network(forms.ModelForm):
    class Meta:
        model = eigrp_network_table
        fields = '__all__'
        labels = {
            'network': 'Allow Network/Wildcard',
            'passive': 'Passive Interface',
            'eigrp': 'EIGRP Name',
        }

    def __init__(self, *args, **kwargs):
        super(forms_eigrp_network, self).__init__(*args, **kwargs)
        self.fields['passive'].empty_label = "-- Select Interface --"
        self.fields['eigrp'].empty_label = "-- Select EIGRP --"


class forms_eigrp_name_network(forms.ModelForm):
    class Meta:
        model = eigrp_table
        fields = '__all__'
        labels = {
            'name': 'Name EIGRP',
            'as_number': 'AS Number',
            'group_routing': 'Group',
        }

    def __init__(self, *args, **kwargs):
        super(forms_eigrp_name_network, self).__init__(*args, **kwargs)
        self.fields['group_routing'].empty_label = "-- Select Group --"


class forms_switchport(forms.ModelForm):
    class Meta:
        model = switchport_table
        fields = '__all__'
        labels = {
            'name': 'SwitchPort name',
            'group_interface': 'Group range Interface',
            'switchport_mode': 'Mode Trunk/Access',
            'vlan': 'VLAN',
            'group_vlan': 'Group range VLAN',
            'group_switchport': 'Group',
        }

    def __init__(self, *args, **kwargs):
        super(forms_switchport, self).__init__(*args, **kwargs)
        self.fields['group_interface'].empty_label = "-- Group range Interface --"
        self.fields['switchport_mode'].empty_label = "-- Select Mode --"
        self.fields['vlan'].empty_label = "-- Select VLAN --"
        self.fields['group_vlan'].empty_label = "-- Group range VLAN --"
        self.fields['group_switchport'].empty_label = "-- Select Group --"


class forms_etherchannel(forms.ModelForm):
    class Meta:
        model = portchannel_table
        fields = '__all__'
        labels = {
            'name': 'EtherChannel name',
            'group_interface': 'Group range Interface',
            'portchannel_number': 'EtherChannel Number',
            'switchport_mode': 'Mode',
            'vlan': 'VLAN',
            'group_vlan': 'Group range VLAN',
            'group_portchannel': 'Group',
        }

    def __init__(self, *args, **kwargs):
        super(forms_etherchannel, self).__init__(*args, **kwargs)
        self.fields['group_interface'].empty_label = "-- Group range Interface --"
        self.fields['switchport_mode'].empty_label = "-- Select Mode --"
        self.fields['vlan'].empty_label = "-- Select VLAN --"
        self.fields['group_vlan'].empty_label = "-- Group range VLAN --"
        self.fields['group_portchannel'].empty_label = "-- Select Group --"
