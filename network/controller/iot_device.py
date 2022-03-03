from decimal import Context
from django.shortcuts import render, redirect
from ..models import *
from django.db import connection
from ..forms import forms_iot, forms_network_type, forms_dhcp, froms_profile, forms_network
from django.db.models import Count


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def iot_list(request):
    cursor = connection.cursor()
    cursor.execute("SELECT network.id AS network_id,iot.id AS id,profile.id as profile_id,network_type.id AS network_type_id,iot.mac AS mac,iot.topic AS topic,iot.subscribe,net.hostname AS hostname,profile.name AS profile,room.room AS room FROM network_iot_table AS iot JOIN network_network_table AS net ON iot.network_id=net.id JOIN network_room_table AS room ON iot.room_id=room.id JOIN network_profile_table AS profile ON iot.profile_id=profile.id JOIN network_network_type_table AS network_type ON network_type.id = net.network_type_id JOIN network_interface_table AS interface ON interface.network_id = net.id JOIN network_network_table AS network ON network.id = iot.network_id GROUP BY iot.id")
    data_all = dictfetchall(cursor)
    data = iot_table.objects.all()
    profile = profile_table.objects.all()
    network = network_table.objects.all()
    room = room_table.objects.all()
    # print(data_all)
    # data_all = iot_table.objects.all().select_related('network')
    # data_select = network_table.objects.all()
    return render(request, 'iot_device/view.html', {
        'data': data,
        'data_all': data_all,
        'profile': profile,
        'network': network,
        'room': room
    })


def iot_add(request):
    mac = request.POST['mac']
    topic = request.POST['topic']
    room = request.POST.get('room_id')
    profile = request.POST.get('profile_id')
    hostname = request.POST.get('network_id')
    add = iot_table.objects.create(
        mac=mac,
        topic=topic,
        room_id=room,
        profile_id=profile,
        network_id=hostname,
    )
    add.save()
    return redirect('/iot_device')


def iot_new(request):
    form = forms_iot()
    if request.method == 'POST':
        form = forms_iot(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/iot_device')
    return render(request, 'iot_device/new.html', {
        'iot': form
    })


def iot_delete(request, id):
    delete = iot_table.objects.get(id=id)
    delete.delete()
    return redirect('/iot_device')


def iot_update(request, pk):
    data = iot_table.objects.get(id=pk)
    form = forms_iot(instance=data)
    if request.method == 'POST':
        form = forms_iot(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/iot_device')
    context = {'form': form}
    return render(request, 'iot_device/update.html', context)


def config(request, id, profile_id, network_type_id, network_id):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT iot.id AS id,iot.topic AS topic,network_type.network_type AS network_type,profile.name AS profile_name,profile.group_vlan_id AS vlan FROM network_iot_table AS iot JOIN network_network_table AS network ON network.id = iot.network_id JOIN network_network_type_table AS network_type ON network_type.id = network.network_type_id JOIN network_profile_table AS profile ON profile.id = iot.profile_id WHERE iot.id = %s", [id])
    data = dictfetchall(cursor)
    # Interface
    interface = connection.cursor()
    interface_sql = "SELECT interface.id,interface.interface,interface.description,interface.ip_netmask,interface.status FROM network_iot_table AS iot JOIN network_network_table AS network ON network.id = iot.network_id JOIN network_interface_table AS interface ON interface.network_id = network.id WHERE iot.id = %s"
    interface_val = (id,)
    interface.execute(interface_sql, interface_val)
    interface_all = dictfetchall(interface)
    # Network
    network = network_table.objects.get(id=network_id)
    networks = forms_network(instance=network)
    # Profile
    profile = profile_table.objects.get(id=profile_id)
    profiles = froms_profile(instance=profile)
    # IoT
    iot = iot_table.objects.get(id=id)
    iots = forms_iot(instance=iot)
    # Network Type
    network_type = network_type_table.objects.get(id=network_type_id)
    network_types = forms_network_type(instance=network_type)
    dhcp = forms_dhcp()
    return render(request, 'iot_device/config.html', {
        'data': data,
        'iot': iots,
        'network_type': network_types,
        'profile': profiles,
        'dhcp': dhcp,
        'network': networks,
        'interface': interface_all,
    })
