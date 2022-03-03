from django.shortcuts import render, redirect
from ..models import group_dhcp_table, group_routing_table, group_acl_table, group_intertrunk_table, group_vlan_table, group_switchport_table, group_portchannel_table
from ..forms import forms_group_dhcp, forms_group_routing, forms_group_access_list, forms_group_sub_interface, forms_group_vlan_table, forms_group_switchport_table, forms_group_portchannel_table
from django.db import connection

# group_dhcp


def group_dhcp(request):
    data = group_dhcp_table.objects.all()
    return render(request, 'group_router/dhcp.html', {'data': data})


def group_dhcp_save(request):
    if request.method == 'POST':
        data = request.POST['name']
        add = group_dhcp_table.objects.create(
            name=data
        )
        add.save()
        return redirect('/group_dhcp')


def group_dhcp_edit(request, pk):
    data = group_dhcp_table.objects.get(id=pk)
    form = forms_group_dhcp(instance=data)
    if request.method == 'POST':
        form = forms_group_dhcp(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/group_dhcp')
    context = {'form': form}
    return render(request, 'group_router/dhcp_edit.html', context)


def group_dhcp_delete(request, pk):
    data = group_dhcp_table.objects.get(id=pk)
    data.delete()
    return redirect('/group_dhcp')

# group_routing


def group_routing(request):
    data = group_routing_table.objects.all()
    return render(request, 'group_router/routing.html', {'data': data})


def group_routing_save(request):
    if request.method == 'POST':
        data = request.POST['name']
        add = group_routing_table.objects.create(
            name=data
        )
        add.save()
        return redirect('/group_routing')


def group_routing_edit(request, pk):
    data = group_routing_table.objects.get(id=pk)
    form = forms_group_routing(instance=data)
    if request.method == 'POST':
        form = forms_group_routing(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/group_routing')
    context = {'form': form}
    return render(request, 'group_router/routing_edit.html', context)


def group_routing_delete(request, pk):
    data = group_routing_table.objects.get(id=pk)
    data.delete()
    return redirect('/group_routing')

# group_access_list


def group_access_list(request):
    data = group_acl_table.objects.all()
    return render(request, 'group_router/access_list.html', {'data': data})


def group_access_list_save(request):
    if request.method == 'POST':
        data = request.POST['name']
        add = group_acl_table.objects.create(
            name=data
        )
        add.save()
        return redirect('/group_access_list')


def group_access_list_edit(request, pk):
    data = group_acl_table.objects.get(id=pk)
    form = forms_group_access_list(instance=data)
    if request.method == 'POST':
        form = forms_group_access_list(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/group_access_list')
    context = {'form': form}
    return render(request, 'group_router/access_list_edit.html', context)


def group_access_list_delete(request, pk):
    data = group_acl_table.objects.get(id=pk)
    data.delete()
    return redirect('/group_access_list')

# group_sub_interface


def group_sub_interface(request):
    data = group_intertrunk_table.objects.all()
    return render(request, 'group_router/sub_interface.html', {'data': data})


def group_sub_interface_save(request):
    if request.method == 'POST':
        data = request.POST['name']
        add = group_intertrunk_table.objects.create(
            name=data
        )
        add.save()
        return redirect('/group_sub_interface')


def group_sub_interface_edit(request, pk):
    data = group_intertrunk_table.objects.get(id=pk)
    form = forms_group_sub_interface(instance=data)
    if request.method == 'POST':
        form = forms_group_sub_interface(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/group_sub_interface')
    context = {'form': form}
    return render(request, 'group_router/sub_interface_edit.html', context)


def group_sub_interface_delete(request, pk):
    data = group_intertrunk_table.objects.get(id=pk)
    data.delete()
    return redirect('/group_sub_interface')

# group_vlan


def group_vlan(request):
    data = group_vlan_table.objects.all()
    return render(request, 'group_switch/vlan.html', {'data': data})


def group_vlan_save(request):
    if request.method == 'POST':
        data = request.POST['name']
        add = group_vlan_table.objects.create(
            name=data
        )
        add.save()
        return redirect('/group_vlan')


def group_vlan_edit(request, pk):
    data = group_vlan_table.objects.get(id=pk)
    form = forms_group_vlan_table(instance=data)
    if request.method == 'POST':
        form = forms_group_vlan_table(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/group_vlan')
    context = {'form': form}
    return render(request, 'group_switch/vlan_edit.html', context)


def group_vlan_delete(request, pk):
    data = group_vlan_table.objects.get(id=pk)
    data.delete()
    return redirect('/group_vlan')

# group_switch_port


def group_switch_port(request):
    data = group_switchport_table.objects.all()
    return render(request, 'group_switch/switch_port.html', {'data': data})


def group_switch_port_save(request):
    if request.method == 'POST':
        data = request.POST['name']
        add = group_switchport_table.objects.create(
            name=data
        )
        add.save()
        return redirect('/group_switch_port')


def group_switch_port_edit(request, pk):
    data = group_switchport_table.objects.get(id=pk)
    form = forms_group_switchport_table(instance=data)
    if request.method == 'POST':
        form = forms_group_switchport_table(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/group_switch_port')
    context = {'form': form}
    return render(request, 'group_switch/switch_port_edit.html', context)


def group_switch_port_delete(request, pk):
    data = group_switchport_table.objects.get(id=pk)
    data.delete()
    return redirect('/group_switch_port')

# group_port_channel


def group_port_channel(request):
    data = group_portchannel_table.objects.all()
    return render(request, 'group_switch/port_channel.html', {'data': data})


def group_port_channel_save(request):
    if request.method == 'POST':
        data = request.POST['name']
        add = group_portchannel_table.objects.create(
            name=data
        )
        add.save()
        return redirect('/group_port_channel')


def group_port_channel_edit(request, pk):
    data = group_portchannel_table.objects.get(id=pk)
    form = forms_group_portchannel_table(instance=data)
    if request.method == 'POST':
        form = forms_group_portchannel_table(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/group_port_channel')
    context = {'form': form}
    return render(request, 'group_switch/port_channel_edit.html', context)


def group_port_channel_delete(request, pk):
    data = group_portchannel_table.objects.get(id=pk)
    data.delete()
    return redirect('/group_port_channel')
