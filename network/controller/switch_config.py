from django.shortcuts import render, redirect
from ..models import *
from ..forms import forms_switchport, forms_etherchannel
from django.db import connection


################ SwitchPort ################

def switchport_list(request):
    data = switchport_table.objects.all()
    return render(request, 'switch_config/switchport/list.html', {
        'switchport': data
    })


def switchport_create(request):
    form = forms_switchport()
    if request.method == 'POST':
        form = forms_switchport(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/switch/switchport')
    return render(request, 'switch_config/switchport/create.html', {
        'switchport': form
    })


def switchport_edit(request, id):
    data = switchport_table.objects.get(pk=id)
    form = forms_switchport(instance=data)
    if request.method == 'POST':
        form = forms_switchport(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/switch/switchport')
    return render(request, 'switch_config/switchport/edit.html', {
        'switchport': form
    })


def switchport_delete(request, id):
    data = switchport_table.objects.get(pk=id)
    data.delete()
    return redirect('/switch/switchport')

################ EtherChannel ################


def etherchannel_list(request):
    data = portchannel_table.objects.all()
    return render(request, 'switch_config/etherchannel/list.html', {
        'etherchannel': data
    })


def etherchannel_create(request):
    form = forms_etherchannel()
    if request.method == 'POST':
        form = forms_etherchannel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/switch/etherchannel')
    return render(request, 'switch_config/etherchannel/create.html', {
        'etherchannel': form
    })


def etherchannel_edit(request, id):
    data = portchannel_table.objects.get(pk=id)
    form = forms_etherchannel(instance=data)
    if request.method == 'POST':
        form = forms_etherchannel(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/switch/etherchannel')
    return render(request, 'switch_config/etherchannel/edit.html', {
        'etherchannel': form
    })


def etherchannel_delete(request, id):
    data = portchannel_table.objects.get(pk=id)
    data.delete()
    return redirect('/switch/etherchannel')
