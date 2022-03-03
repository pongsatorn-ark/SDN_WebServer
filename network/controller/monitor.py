from django.shortcuts import render, redirect
from ..models import tudo_table
import paho.mqtt.publish as mqtt_pub

hostname = "172.16.20.12"
port = 1883
# Create your views here.
mqtt_auth = {
    'username': 'administrator',
    'password': 'P@ssw0rd@DevNet'
}


def dashboard(request):
    data = tudo_table.objects.all()
    return render(request, 'dashboard/dashboard.html', {'data': data})


def dashboard_deploy(request):
    data = request.POST['command']
    # print(data)
    data_send("/10:02:B5:99:25:5F/SDN", data)
    # data_send("/30:AE:A4:03:3C:CC/SDN", data)
    return redirect('/')


def data_send(topic, msg):
    mqtt_pub.single(topic, msg, qos=0, hostname="172.16.20.12",
                    port=1883, auth=mqtt_auth)
