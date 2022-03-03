from django.shortcuts import render, redirect
from ..models import profile_table
from django.db import connection
from ..forms import froms_profile
cursor = connection.cursor()


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def profile_list(request):
    cursor.execute("SELECT * FROM network_profile_table")
    data = dictfetchall(cursor)
    data2 = profile_table.objects.all()
    return render(request, 'profile/view.html', {'data': data, 'data2': data2})


def profile_new(request):
    form = froms_profile()
    if request.method == 'POST':
        form = froms_profile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    return render(request, 'profile/new.html', {
        'profile': form
    })


# def profile_save(request):
#     if request.POST:
#         profile = request.POST['profile']
#         domain_lookup = request.POST.get('domain_lookup', '') == 'on'
#         service_pwd = request.POST.get('service_pwd', '') == 'on'
#         domain_name = request.POST['domain_name']
#         add = profile_table.objects.create(
#             name=profile,
#             domain_lookup=domain_lookup,
#             service_pwd=service_pwd,
#             domain_name=domain_name,
#         )
#         add.save()
#         return redirect('/profile')


def profile_delete(request, id):
    delete = profile_table.objects.get(id=id)
    delete.delete()
    return redirect('/profile')


def profile_update(request, pk):
    data = profile_table.objects.get(id=pk)
    form = froms_profile(instance=data)
    if request.method == 'POST':
        form = froms_profile(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    return render(request, 'profile/update.html', {
        'profile': form
    })
