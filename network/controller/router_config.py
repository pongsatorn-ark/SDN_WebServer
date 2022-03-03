from django.shortcuts import render, redirect
from ..models import *
from ..forms import forms_dhcp, forms_eigrp_network, forms_hsrp, forms_sub_interface, forms_static, forms_eigrp_name_network
from django.db import connection


################ DHCP ################

def dhcp_list(request):
    data = dhcp_table.objects.all()
    return render(request, 'router_config/dhcp/list.html', {
        'data': data
    })


def dhcp_create(request):
    form = forms_dhcp()
    if request.method == 'POST':
        form = forms_dhcp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/router/dhcp')
    return render(request, 'router_config/dhcp/create.html', {
        'form': form
    })


def dhcp_edit(request, id):
    data = dhcp_table.objects.get(pk=id)
    form = forms_dhcp(instance=data)
    if request.method == 'POST':
        form = forms_dhcp(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/router/dhcp')
    return render(request, 'router_config/dhcp/edit.html', {
        'form': form
    })


def dhcp_delete(request, id):
    data = dhcp_table.objects.get(pk=id)
    data.delete()
    return redirect('/router/dhcp')

################ HSRP ################


def hsrp_list(request):
    data = hsrp_table.objects.all()
    return render(request, 'router_config/hsrp/list.html', {
        'hsrp': data
    })


def hsrp_create(request):
    form = forms_hsrp()
    if request.method == 'POST':
        form = forms_hsrp(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/router/hsrp')
    return render(request, 'router_config/hsrp/create.html', {
        'hsrp': form
    })


def hsrp_edit(request, id):
    data = hsrp_table.objects.get(pk=id)
    form = forms_hsrp(instance=data)
    if request.method == 'POST':
        form = forms_hsrp(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/router/hsrp')
    return render(request, 'router_config/hsrp/edit.html', {
        'hsrp': form
    })


def hsrp_delete(request, id):
    data = hsrp_table.objects.get(pk=id)
    data.delete()
    return redirect('/router/hsrp')

################ Sub Interface ################


def sub_interface_list(request):
    data = intertrunk_table.objects.all()
    return render(request, 'router_config/trunk/list.html', {
        'sub_interface': data
    })


def sub_interface_create(request):
    form = forms_sub_interface()
    if request.method == 'POST':
        form = forms_sub_interface(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/router/sub_interface')
    return render(request, 'router_config/trunk/create.html', {
        'sub_interface': form
    })


def sub_interface_edit(request, id):
    data = intertrunk_table.objects.get(pk=id)
    form = forms_sub_interface(instance=data)
    if request.method == 'POST':
        form = forms_sub_interface(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/router/sub_interface')
    return render(request, 'router_config/trunk/edit.html', {
        'sub_interface': form
    })


def sub_interface_delete(request, id):
    data = intertrunk_table.objects.get(pk=id)
    data.delete()
    return redirect('/router/sub_interface')

################ Static Route ################


def static_list(request):
    data = static_route_table.objects.all()
    return render(request, 'routing/static_route/list.html', {
        'static': data
    })


def static_create(request):
    form = forms_static()
    if request.method == 'POST':
        form = forms_static(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/router/static_route')
    return render(request, 'routing/static_route/create.html', {
        'static': form
    })


def static_edit(request, id):
    data = static_route_table.objects.get(pk=id)
    form = forms_static(instance=data)
    if request.method == 'POST':
        form = forms_static(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/router/static_route')
    return render(request, 'routing/static_route/edit.html', {
        'static': form
    })


def static_delete(request, id):
    data = static_route_table.objects.get(pk=id)
    data.delete()
    return redirect('/router/static_route')

 # EIGRP Route ################


def eigrp_list(request):
    data = eigrp_network_table.objects.all()
    return render(request, 'routing/eigrp/list.html', {
        'eigrp': data
    })


def eigrp_create(request):
    form = forms_eigrp_network()
    if request.method == 'POST':
        form = forms_eigrp_network(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/router/eigrp')
    return render(request, 'routing/eigrp/create.html', {
        'eigrp': form
    })


def eigrp_edit(request, id):
    data = eigrp_network_table.objects.get(pk=id)
    form = forms_eigrp_network(instance=data)
    if request.method == 'POST':
        form = forms_eigrp_network(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/router/eigrp')
    return render(request, 'routing/eigrp/edit.html', {
        'eigrp': form
    })


def eigrp_delete(request, id):
    data = eigrp_network_table.objects.get(pk=id)
    data.delete()
    return redirect('/router/eigrp')


def eigrp_create_name(request):
    form = forms_eigrp_name_network()
    if request.method == 'POST':
        form = forms_eigrp_name_network(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/router/eigrp/add')
    return render(request, 'routing/eigrp/create_eigrp.html', {
        'eigrp_name': form
    })
