from typing import overload
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TimeField
from django.forms.utils import from_current_timezone, to_current_timezone
# Create your models here.


class group_routing_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group Routing"
        verbose_name_plural = "Group Routing"


class eigrp_table(models.Model):
    name = models.CharField(max_length=50, null=True)
    as_number = models.CharField(max_length=100, null=True)
    group_routing = models.ForeignKey(
        group_routing_table, on_delete=CASCADE, null=True, blank=True, related_name='eigrp')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "EIGRP Routing"
        verbose_name_plural = "Routing EIGRP"


class static_route_table(models.Model):
    name = models.CharField(max_length=50, null=True)
    network_netmask_route = models.CharField(max_length=100, null=True)
    group_routing = models.ForeignKey(
        group_routing_table, on_delete=CASCADE, null=True, blank=True, related_name='static_route')


class group_intertrunk_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group Sub-interface Trunk"
        verbose_name_plural = "Group Sub-interface Trunk"


class group_acl_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group Access Control List"
        verbose_name_plural = "Group Access Control List"


class group_dhcp_table(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group DHCP"
        verbose_name_plural = "Group DHCP"


class group_switchport_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group Switch Port"
        verbose_name_plural = "Group Switch Port"


class group_portchannel_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group Port Channel"
        verbose_name_plural = "Group Port Channel"


class group_interface_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group Interface"
        verbose_name_plural = "Group Interface"


class eigrp_network_table(models.Model):
    eigrp = models.ForeignKey(
        eigrp_table, on_delete=CASCADE, null=True, blank=True, related_name='eigrp_network')
    network = models.CharField(max_length=100, null=True)
    passive = models.ForeignKey(
        group_interface_table, on_delete=CASCADE, null=True, blank=True, related_name='eigrp_network')


class switchport_mode_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Switch Port Mode"
        verbose_name_plural = "Switch Port Mode"


class username_table(models.Model):
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username+" "+self.password

    class Meta:
        ordering = ('id',)
        verbose_name = "Username Password"
        verbose_name_plural = "Username Password"


class group_vlan_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Group VLAN"
        verbose_name_plural = "Group VLAN"


class vlan_table(models.Model):
    vlan_number = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    group_vlan = models.ForeignKey(
        group_vlan_table, on_delete=CASCADE, null=True, related_name='vlan')

    def __str__(self):
        return self.vlan_number+" "+self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "VLAN"
        verbose_name_plural = "VLAN"


class switchport_table(models.Model):
    name = models.CharField(max_length=50, null=True)
    group_interface = models.ForeignKey(
        group_interface_table, on_delete=CASCADE, null=True, blank=True, related_name='switch_port')
    switchport_mode = models.ForeignKey(
        switchport_mode_table, on_delete=CASCADE, null=True, blank=True, related_name='switch_port')
    vlan = models.ForeignKey(
        vlan_table, on_delete=CASCADE, null=True, blank=True, related_name='switch_port')
    group_vlan = models.ForeignKey(
        group_vlan_table, on_delete=CASCADE, null=True, blank=True, related_name='switch_port')
    group_switchport = models.ForeignKey(
        group_switchport_table, on_delete=CASCADE, null=True, blank=True, related_name='switch_port')

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ('id',)
    #     verbose_name = "SwitchPort Trunk/Access"
    #     verbose_name_plural = "SwitchPort Trunk/Access"


class portchannel_table(models.Model):
    name = models.CharField(max_length=50, null=True)
    group_interface = models.ForeignKey(
        group_interface_table, on_delete=CASCADE, null=True, blank=True, related_name='portchannel')
    portchannel_number = models.CharField(max_length=50)
    switchport_mode = models.ForeignKey(
        switchport_mode_table, on_delete=CASCADE, null=True, blank=True, related_name='portchannel')
    vlan = models.ForeignKey(
        vlan_table, on_delete=CASCADE, null=True, blank=True, related_name='portchannel')
    group_vlan = models.ForeignKey(
        group_vlan_table, on_delete=CASCADE, null=True, blank=True, related_name='portchannel')
    group_portchannel = models.ForeignKey(
        group_portchannel_table, on_delete=CASCADE, null=True, blank=True, related_name='portchannel')

    def __str__(self):
        return self.name


class room_table(models.Model):
    room = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.room

    class Meta:
        ordering = ('id',)
        verbose_name = "Room"
        verbose_name_plural = "Room"


class interface_type_table(models.Model):
    interface_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.interface_type

    class Meta:
        ordering = ('id',)
        verbose_name = "Interface Type"
        verbose_name_plural = "Interface Type"


class network_type_table(models.Model):
    network_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.network_type

    class Meta:
        ordering = ('id',)
        verbose_name = "Device Type"
        verbose_name_plural = "Device Type"


class profile_table(models.Model):
    name = models.CharField(max_length=50, null=True)
    domain_lookup = models.BooleanField(default=False)
    service_pwd = models.BooleanField(default=False)
    domain_name = models.CharField(max_length=50, null=True)
    default_gateway = models.CharField(max_length=50, null=True, blank=True)
    ssh = models.BooleanField(default=False)
    neighbor = models.BooleanField(default=False)
    username = models.ForeignKey(
        username_table, on_delete=CASCADE, null=True, blank=True, related_name='profile')
    console = models.BooleanField(default=False)
    vty = models.BooleanField(default=False)
    group_vlan = models.ForeignKey(
        group_vlan_table, on_delete=CASCADE, null=True, blank=True, related_name='profile')
    group_switchport = models.ForeignKey(
        group_switchport_table, on_delete=CASCADE, null=True, blank=True, related_name='profile')
    group_portchannel = models.ForeignKey(
        group_portchannel_table, on_delete=CASCADE, null=True, blank=True, related_name='profile')
    group_routing = models.ForeignKey(
        group_routing_table, on_delete=CASCADE, blank=True, null=True, related_name='profile')
    group_acl = models.ForeignKey(
        group_acl_table, on_delete=CASCADE, null=True, blank=True, related_name='profile')
    group_intertrunk = models.ForeignKey(
        group_intertrunk_table, on_delete=CASCADE, null=True, blank=True, related_name='profile')
    group_dhcp = models.ForeignKey(
        group_dhcp_table, on_delete=CASCADE, null=True, blank=True, related_name='profile')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class network_table(models.Model):
    hostname = models.CharField(max_length=50, null=True)
    pid = models.CharField(max_length=50, null=True)
    sn = models.CharField(max_length=50, null=True)
    network_type = models.ForeignKey(
        network_type_table, on_delete=CASCADE, null=True, blank=True, related_name='network')
    interface_type = models.ForeignKey(
        interface_type_table, on_delete=CASCADE, null=True, blank=True, related_name='network')

    def __str__(self):
        return self.hostname

    class Meta:
        ordering = ('id',)
        verbose_name = "Network Device"
        verbose_name_plural = "Network Device"


class interface_table(models.Model):
    interface = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    ip_netmask = models.CharField(max_length=50, null=True, blank=True)
    status = models.BooleanField(default=False)
    network = models.ForeignKey(
        network_table, on_delete=CASCADE, null=True, blank=True, related_name='interface')
    access = models.ForeignKey(
        vlan_table, on_delete=CASCADE, null=True, blank=True, related_name='interface')
    # group_interface = models.ForeignKey(
    #     group_interface_table, on_delete=CASCADE, null=True, blank=True, related_name='interface')

    def interface_sum(self):
        return f"{self.interface} {self.network}"

    def __str__(self):
        return self.interface_sum()

    class Meta:
        ordering = ("id",)
        verbose_name = "Interface Device"
        verbose_name_plural = "Interface Device"


class dhcp_table(models.Model):
    excluded = models.CharField(max_length=50, null=True)
    dhcp_pool = models.CharField(max_length=50, null=True)
    interface_helper = models.ForeignKey(
        interface_table, on_delete=CASCADE, blank=True, null=True, related_name='dhcp')
    helper_address = models.CharField(max_length=50, null=True, blank=True)
    network = models.CharField(max_length=50, null=True)
    default_router = models.CharField(max_length=50, null=True)
    dns_server = models.CharField(max_length=50, null=True, blank=True)
    domain_name = models.CharField(max_length=50, null=True)
    group_dhcp = models.ForeignKey(
        group_dhcp_table, on_delete=CASCADE, null=True, blank=True, related_name='dhcp')

    class Meta:
        ordering = ("id",)
        verbose_name = "Configuration DHCP"
        verbose_name_plural = "Configuration DHCP"


class intertrunk_table(models.Model):
    interface = models.ForeignKey(
        interface_table, on_delete=CASCADE, blank=True, null=True, related_name='intertrunk')
    sub_interface = models.CharField(max_length=50, null=True)
    vlan = models.ForeignKey(
        vlan_table, on_delete=CASCADE, blank=True, null=True, related_name='intertrunk')
    address = models.CharField(max_length=50, null=True)
    group_intertrunk = models.ForeignKey(
        group_intertrunk_table, on_delete=CASCADE, blank=True, null=True, related_name='intertrunk')

    class Meta:
        ordering = ("id",)
        verbose_name = "Sub-Interface"
        verbose_name_plural = "Sub-Interface"


class hsrp_table(models.Model):
    interface = models.ForeignKey(
        interface_table, on_delete=CASCADE, null=True, blank=True, related_name='hsrp')
    standby_number = models.CharField(max_length=50, null=True)
    vip = models.CharField(max_length=50, null=True)
    priority = models.CharField(max_length=50, null=True)


class nat_pool_table(models.Model):
    name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    netmask = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class acl_table(models.Model):
    name = models.CharField(max_length=50, null=True)
    std_exten = models.BooleanField(default=False)
    interface_in = models.BooleanField(default=False)
    interface_out = models.BooleanField(default=False)
    interface = models.ForeignKey(
        interface_table, on_delete=CASCADE, null=True, blank=True, related_name='acl')
    group_acl = models.ForeignKey(
        group_acl_table, on_delete=CASCADE, null=True, blank=True, related_name='acl')

    def __str__(self):
        return self.acl_table


class nat_pat_table(models.Model):
    nat_pool = models.ForeignKey(
        nat_pool_table, on_delete=CASCADE, null=True, blank=True, related_name='nat_pat')
    acl = models.ForeignKey(
        acl_table, on_delete=CASCADE, null=True, blank=True, related_name='nat_pat')
    overload = models.BooleanField(default=False)
    interface_in = models.BooleanField(default=False)
    interface_out = models.BooleanField(default=False)
    interface = models.ForeignKey(
        interface_table, on_delete=CASCADE, null=True, blank=True, related_name='nat_pat')


class protocal_table(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = "Protocal"
        verbose_name_plural = "Protocal"
        # db_table = "protocal_table"


class acl_policy_table(models.Model):
    specify = models.BooleanField(default=False)
    protocal = models.ForeignKey(
        protocal_table, on_delete=CASCADE, null=True, blank=True, related_name='acl_policy')
    any = models.BooleanField(default=False)
    src_address = models.CharField(max_length=50, null=True)
    des_any = models.BooleanField(default=False)
    host = models.BooleanField(default=False)
    src_port = models.CharField(max_length=50, null=True)
    des_address = models.CharField(max_length=50, null=True)
    range_port = models.BooleanField(default=False)
    des_port = models.CharField(max_length=50, null=True)
    acl = models.ForeignKey(
        acl_table, on_delete=CASCADE, null=True, blank=True, related_name='acl_policy')


class iot_table(models.Model):
    mac = models.CharField(max_length=50, null=True)
    topic = models.CharField(max_length=50, null=True)
    subscribe = models.CharField(max_length=50, null=True)
    room = models.ForeignKey(
        room_table, on_delete=CASCADE, null=True, blank=True, related_name='iot')
    profile = models.ForeignKey(
        profile_table, on_delete=CASCADE, null=True, blank=True, related_name='iot')
    network = models.ForeignKey(
        network_table, on_delete=CASCADE, null=True, blank=True, related_name='iot')
    lb_min = models.BooleanField(default=False)
    lb_max = models.BooleanField(default=False)
    lb_avg = models.BooleanField(default=False)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('id',)
        verbose_name = "IoT Device"
        verbose_name_plural = "IoT Device"
        # db_table = "protocal_table"


class tudo_table(models.Model):
    iot = models.ForeignKey(
        iot_table, on_delete=CASCADE, null=True, blank=True, related_name='tudo')
    command = models.CharField(max_length=60, null=True)
    start = models.DateTimeField(auto_now=True, null=True)
    end = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "Event Log"
        verbose_name_plural = "Event Log"
        # db_table = "protocal_table"


# class topology_table(models.Model):
#     topic = models.ForeignKey(
#         iot_table, on_delete=CASCADE, null=False)
#     interface = models.ManyToManyField(interface_table, blank=True)
#     vlan = models.ManyToManyField(vlan_table, blank=True)

#     class Meta:
#         ordering = ('id',)
#         verbose_name = "Topology"
#         verbose_name_plural = "Topology"


class traffic_interface_table(models.Model):
    interface = models.ForeignKey(
        interface_table, on_delete=CASCADE, null=True, blank=True, related_name='traffic_interface')
    RXBS = models.CharField(max_length=50, null=True, blank=True)
    TXBS = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "Traffic Interface"
        verbose_name_plural = "Traffic Interface"


class load_balance_stp_table(models.Model):
    switch = models.ForeignKey(network_table, on_delete=CASCADE,
                               null=True, blank=True, related_name='traffic_interface')
    root_bridge = models.CharField(max_length=50, null=True, blank=True)
    command = models.CharField(max_length=50, null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "STP LB"
        verbose_name_plural = "STP LB"


class different_table(models.Model):
    different = models.CharField(max_length=50, null=True, blank=True)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "Different LB"
        verbose_name_plural = "Different LB"


class count_table(models.Model):
    switch = models.ForeignKey(network_table, on_delete=CASCADE,
                               null=True, blank=True, related_name='count')
    count = models.IntegerField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name = "Count LB"
        verbose_name_plural = "Count LB"
