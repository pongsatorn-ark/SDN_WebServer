from django.shortcuts import redirect, render
from ..models import interface_table, network_table, interface_type_table, network_type_table
from ..forms import forms_network
# Create your views here.


def network_list(request):
    data_network = network_table.objects.all().select_related(
        'interface_type').select_related('network_type')
    return render(request, 'network_device/view.html', {'data_network': data_network})


def network_new(request):
    interface_type = interface_type_table.objects.all()
    network_type = network_type_table.objects.all()
    return render(request, 'network_device/new.html', {'data1': interface_type, 'data2': network_type})


def network_save(request):
    if request.POST:
        hostname = request.POST['hostname']
        pid = request.POST['pid']
        sn = request.POST['sn']
        interface = request.POST.get('interface_type')
        network = request.POST.get('network_type')
        add = network_table.objects.create(
            hostname=hostname,
            pid=pid,
            sn=sn,
            interface_type_id=interface,
            network_type_id=network,
        )
        add.save()
        return redirect('/network_device')


def network_delete(request, id):
    delete = network_table.objects.get(id=id)
    delete.delete()
    return redirect('/network_device')


def network_generate(request, pk):
    data = network_table.objects.get(id=pk)
    if data.interface_type.interface_type == "cisco-1841":
        number = ['FastEthernet0/0', 'FastEthernet0/1']
        for i in number:
            add = interface_table.objects.create(
                interface=i,
                network_id=data.id,
            )
            add.save()
    if data.interface_type.interface_type == "ws-c2960-24-s":
        number = ['vlan 1', 'FastEthernet0/1', 'FastEthernet0/2', 'FastEthernet0/3', 'FastEthernet0/4', 'FastEthernet0/5', 'FastEthernet0/6', 'FastEthernet0/7', 'FastEthernet0/8', 'FastEthernet0/9', 'FastEthernet0/10', 'FastEthernet0/11', 'FastEthernet0/12',
                  'FastEthernet0/13', 'FastEthernet0/14', 'FastEthernet0/15', 'FastEthernet0/16', 'FastEthernet0/17', 'FastEthernet0/18', 'FastEthernet0/19', 'FastEthernet0/20', 'FastEthernet0/21', 'FastEthernet0/22', 'FastEthernet0/23', 'FastEthernet0/24']
        for i in number:
            add = interface_table.objects.create(
                interface=i,
                network_id=data.id,
            )
            add.save()
    if data.interface_type.interface_type == "WS-C2960-24TC-L":
        number = ['vlan 1', 'FastEthernet0/1', 'FastEthernet0/2', 'FastEthernet0/3', 'FastEthernet0/4', 'FastEthernet0/5', 'FastEthernet0/6', 'FastEthernet0/7', 'FastEthernet0/8', 'FastEthernet0/9', 'FastEthernet0/10', 'FastEthernet0/11', 'FastEthernet0/12',
                  'FastEthernet0/13', 'FastEthernet0/14', 'FastEthernet0/15', 'FastEthernet0/16', 'FastEthernet0/17', 'FastEthernet0/18', 'FastEthernet0/19', 'FastEthernet0/20', 'FastEthernet0/21', 'FastEthernet0/22', 'FastEthernet0/23', 'FastEthernet0/24', 'GigabitEthernet0/1', 'GigabitEthernet0/2']
        for i in number:
            add = interface_table.objects.create(
                interface=i,
                network_id=data.id,
            )
            add.save()
    if data.interface_type.interface_type == "ws-c2960-48TT-L":
        number = ['vlan 1', 'FastEthernet0/1', 'FastEthernet0/2', 'FastEthernet0/3', 'FastEthernet0/4', 'FastEthernet0/5', 'FastEthernet0/6', 'FastEthernet0/7', 'FastEthernet0/8', 'FastEthernet0/9', 'FastEthernet0/10', 'FastEthernet0/11', 'FastEthernet0/12', 'FastEthernet0/13', 'FastEthernet0/14', 'FastEthernet0/15', 'FastEthernet0/16', 'FastEthernet0/17', 'FastEthernet0/18', 'FastEthernet0/19', 'FastEthernet0/20', 'FastEthernet0/21', 'FastEthernet0/22', 'FastEthernet0/23', 'FastEthernet0/24', 'FastEthernet0/25',
                  'FastEthernet0/26', 'FastEthernet0/27', 'FastEthernet0/28', 'FastEthernet0/29', 'FastEthernet0/30', 'FastEthernet0/31', 'FastEthernet0/32', 'FastEthernet0/33', 'FastEthernet0/34', 'FastEthernet0/35', 'FastEthernet0/36', 'FastEthernet0/37', 'FastEthernet0/38', 'FastEthernet0/39', 'FastEthernet0/40', 'FastEthernet0/41', 'FastEthernet0/42', 'FastEthernet0/43', 'FastEthernet0/44', 'FastEthernet0/45', 'FastEthernet0/46', 'FastEthernet0/47', 'FastEthernet0/48', 'GigabitEthernet0/1', 'GigabitEthernet0/2']
        for i in number:
            add = interface_table.objects.create(
                interface=i,
                network_id=data.id,
            )
            add.save()
    return redirect('/network_device')


def network_update(request, pk):
    data = network_table.objects.get(id=pk)
    form = forms_network(instance=data)
    if request.method == 'POST':
        form = forms_network(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/network_device')
    context = {'form': form}
    return render(request, 'network_device/update.html', context)
