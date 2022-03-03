from django.shortcuts import render, redirect
from ..models import iot_table, network_table, network_type_table, profile_table, room_table, tudo_table
import paho.mqtt.publish as mqtt_pub
import paho.mqtt.subscribe as mqtt_sub
from django.db import connection
import datetime
import paho.mqtt.client as mqtt
import time
from django.shortcuts import render, redirect
hostname = "172.16.20.12"
port = 1883
# Create your views here.
mqtt_auth = {
    'username': 'administrator',
    'password': 'P@ssw0rd@DevNet'
}

mes_error = None
# start_time = time.time()


def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def deploy_config(request, id):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT network_type.network_type AS network_type,iot.id AS id, profile.id AS pid,nettable.hostname AS hostname,nettable.id AS nid,iot.topic AS topic,profile.domain_name AS domain_name,profile.domain_lookup AS domain_lookup,profile.service_pwd AS pwd,profile.ssh AS ssh,user.username AS user,user.password password,profile.default_gateway AS df,profile.vty AS vty,profile.console AS console,profile.neighbor AS neighbor FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id WHERE iot.id = %s", [id])
    data = dictfetchall(cursor)
    data_all = ['configure terminal']
    interface = connection.cursor()
    sql_interface = "SELECT interface.interface AS interface , interface.description AS description,interface.ip_netmask AS address,interface.status AS status FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id JOIN network_interface_table AS interface ON interface.network_id = nettable.id WHERE iot.id = %s AND interface.ip_netmask IS NOT NULL"
    val_interface = (id,)
    vlan = connection.cursor()
    sql_vlan = "SELECT iot.id AS id,vlan.vlan_number AS number,vlan.name AS name FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id JOIN network_interface_table AS interface ON interface.network_id = nettable.id JOIN network_group_vlan_table AS group_vlan ON group_vlan.id = profile.group_vlan_id JOIN network_vlan_table AS vlan ON vlan.group_vlan_id = group_vlan.id WHERE iot.id = %s GROUP BY vlan.vlan_number"
    val_vlan = (id,)
    vlan.execute(sql_vlan, val_vlan)
    vlan_all = dictfetchall(vlan)
    interface.execute(sql_interface, val_interface)
    interface_all = dictfetchall(interface)
    # assign data to list
    for i in data:
        if i['network_type'] == "Switch":
            if i['hostname'] == "":
                pass
            else:
                data_all.append('hostname' + " " + i['hostname'])
            if i['domain_name'] == "":
                pass
            else:
                data_all.append('ip domain-name' + " " + i['domain_name'])
            if i['ssh'] == 1:
                data_all.append(
                    'username' + " " + i['user']+" "+'privilege 15 secret' + " " + i['password'])
            if i['df'] == None:
                pass
            else:
                data_all.append('ip default-gateway' + " " + i['df'])
            if i['domain_lookup'] == 1:
                data_all.append('no ip domain-lookup')
            if i['pwd'] == 1:
                data_all.append('service password-encryption')
            if i['vty'] == 1:
                data_all.append('line vty 0 15')
                data_all.append('transport input telnet ssh')
                data_all.append('login local')
            if i['console'] == 1:
                data_all.append('line console 0')
                data_all.append('password P@ssw0rd@iot')
                data_all.append('login')
                data_all.append('no logging synchronous')
                data_all.append('exec-timeout 15 0')
                data_all.append('exit')
            if i['neighbor'] == 1:
                data_all.append('cdp run')
                data_all.append('lldp run')
            for i in vlan_all:
                if i['number'] != None:
                    data_all.append('vlan'+" "+i['number'])
                if i['name'] != None:
                    data_all.append('name'+" "+i['name'])
            for interface in interface_all:
                if interface['status'] == 1:
                    data_all.append('interface'+" "+interface['interface'])
                    data_all.append('description'+" "+interface['description'])
                    data_all.append('ip address'+" "+interface['address'])
                    data_all.append('no shutdown')
            data_all.append('exit')
            data_all.append('crypto key generate rsa modulus 1024')
            data_all.append('spanning-tree mode rapid-pvst')
            data_all.append('end')
            data_all.append('wr')
        elif i['network_type'] == "Router":
            print(i['network_type'])
            if i['hostname'] == "":
                pass
            else:
                data_all.append('hostname' + " " + i['hostname'])
            if i['domain_name'] == "":
                pass
            else:
                data_all.append('ip domain-name' + " " + i['domain_name'])
            if i['ssh'] == 1:
                data_all.append(
                    'username' + " " + i['user']+" "+'privilege 15 secret' + " " + i['password'])
            if i['df'] == None:
                pass
            else:
                data_all.append('ip default-gateway' + " " + i['df'])
            if i['domain_lookup'] == 1:
                data_all.append('no ip domain-lookup')
            if i['pwd'] == 1:
                data_all.append('service password-encryption')
            if i['vty'] == 1:
                data_all.append('line vty 0 15')
                data_all.append('transport input telnet ssh')
                data_all.append('login local')
            if i['console'] == 1:
                data_all.append('line console 0')
                data_all.append('password P@ssw0rd@iot')
                data_all.append('login')
                data_all.append('no logging synchronous')
                data_all.append('exit')
            if i['neighbor'] == 1:
                data_all.append('cdp run')

            data_all.append('crypto key generate rsa modulus 1024')
            data_all.append('end')
            data_all.append('wr')
    for tudo in data_all:
        for i in data:
            now = datetime.datetime.now()
            list = connection.cursor()
            sql = "insert into network_tudo_table (command,start,iot_id) values (%s,%s,%s)"
            val = (tudo, now, i['id'])
            list.execute(sql, val)
            connection.commit()
    deploy_basic(id)
    return redirect('/')


def deploy_vlan(request, id):
    vlan = connection.cursor()
    vlan_id = connection.cursor()
    sql_vlan = "SELECT iot.id AS id,vlan.vlan_number AS number,vlan.name AS name FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id JOIN network_interface_table AS interface ON interface.network_id = nettable.id JOIN network_group_vlan_table AS group_vlan ON group_vlan.id = profile.group_vlan_id JOIN network_vlan_table AS vlan ON vlan.group_vlan_id = group_vlan.id WHERE iot.id = %s GROUP BY vlan.vlan_number"
    sql_id = "SELECT iot.id AS id FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id JOIN network_interface_table AS interface ON interface.network_id = nettable.id JOIN network_group_vlan_table AS group_vlan ON group_vlan.id = profile.group_vlan_id JOIN network_vlan_table AS vlan ON vlan.group_vlan_id = group_vlan.id WHERE iot.id = %s GROUP BY iot.id"
    val_vlan = (id,)
    val_id = (id,)
    vlan.execute(sql_vlan, val_vlan)
    vlan_id.execute(sql_id, val_id)
    vlan_id_all = dictfetchall(vlan_id)
    vlan_all = dictfetchall(vlan)
    data_all = ['configure terminal']
    for i in vlan_all:
        if i['number'] != None:
            data_all.append('vlan'+" "+i['number'])
        if i['name'] != None:
            data_all.append('name'+" "+i['name'])
    data_all.append('end')
    data_all.append('wr')
    for tudo in data_all:
        for i in vlan_id_all:
            now = datetime.datetime.now()
            list = connection.cursor()
            sql = "insert into network_tudo_table (command,start,iot_id) values (%s,%s,%s)"
            val = (tudo, now, i['id'])
            list.execute(sql, val)
            connection.commit()
    deploy_basic(id)
    return redirect('/')


def deploy_hostname(request, id):
    hostname = connection.cursor()
    # vlan_id = connection.cursor()
    sql_hostname = "SELECT iot.id AS id,nettable.hostname AS hostname,profile.domain_name AS domain_name FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id WHERE iot.id = %s"
    # sql_id = "SELECT iot.id AS id FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id JOIN network_interface_table AS interface ON interface.network_id = nettable.id JOIN network_group_vlan_table AS group_vlan ON group_vlan.id = profile.group_vlan_id JOIN network_vlan_table AS vlan ON vlan.group_vlan_id = group_vlan.id WHERE iot.id = %s GROUP BY iot.id"
    val_hostname = (id,)
    # val_id = (id,)
    hostname.execute(sql_hostname, val_hostname)
    # vlan_id.execute(sql_id, val_id)
    # vlan_id_all = dictfetchall(vlan_id)
    hostname_domain = dictfetchall(hostname)
    data_all = ['configure terminal']
    for i in hostname_domain:
        if i['hostname'] != None:
            data_all.append('hostname' + " " + i['hostname'])
        if i['domain_name'] != None:
            data_all.append('ip domain-name' + " " + i['domain_name'])
    data_all.append('end')
    data_all.append('wr')
    for tudo in data_all:
        for i in hostname_domain:
            now = datetime.datetime.now()
            list = connection.cursor()
            sql = "insert into network_tudo_table (command,start,iot_id) values (%s,%s,%s)"
            val = (tudo, now, i['id'])
            list.execute(sql, val)
            connection.commit()
            # print(now, "insert")
    deploy_basic(id)
    return redirect('/')


def deploy_interface(request, id):
    interface = connection.cursor()
    # vlan_id = connection.cursor()
    sql_interface = "SELECT iot.id,interface.interface,interface.description,interface.ip_netmask,interface.status,vlan.vlan_number AS access FROM network_iot_table AS iot JOIN network_network_table AS network ON network.id = iot.network_id JOIN network_interface_table AS interface ON interface.network_id = network.id LEFT JOIN network_vlan_table AS vlan ON vlan.id = interface.access_id WHERE interface.id = %s"
    # sql_id = "SELECT iot.id AS id FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id JOIN network_interface_table AS interface ON interface.network_id = nettable.id JOIN network_group_vlan_table AS group_vlan ON group_vlan.id = profile.group_vlan_id JOIN network_vlan_table AS vlan ON vlan.group_vlan_id = group_vlan.id WHERE iot.id = %s GROUP BY iot.id"
    val_interface = (id,)
    # val_id = (id,)
    interface.execute(sql_interface, val_interface)
    # vlan_id.execute(sql_id, val_id)
    # vlan_id_all = dictfetchall(vlan_id)
    interface_all = dictfetchall(interface)
    data_all = ['configure terminal']
    iot_id = None
    for interface in interface_all:
        print(interface)
        if interface['ip_netmask'] != None and interface['status'] == 1:
            data_all.append('interface'+" "+interface['interface'])
            data_all.append('description'+" "+interface['description'])
            data_all.append('ip address'+" "+interface['ip_netmask'])
            data_all.append('no shutdown')
        elif interface['status'] == 1:
            data_all.append('interface'+" "+interface['interface'])
            data_all.append('no shutdown')
        elif interface['access'] != None and interface['status'] == 1:
            data_all.append('interface'+" "+interface['interface'])
            data_all.append('description'+" "+interface['description'])
            data_all.append('switchport mode access')
            data_all.append('switchport access vlan'+" "+interface['access'])
            data_all.append('no shutdown')
        iot_id = interface['id']
    data_all.append('end')
    data_all.append('wr')
    for tudo in data_all:
        for i in interface_all:
            now = datetime.datetime.now()
            list = connection.cursor()
            sql = "insert into network_tudo_table (command,start,iot_id) values (%s,%s,%s)"
            val = (tudo, now, i['id'])
            list.execute(sql, val)
            connection.commit()
    deploy_basic(iot_id)
    return redirect('/')


def deploy_interface_all(request, id):
    interface = connection.cursor()
    # vlan_id = connection.cursor()
    sql_interface = "SELECT iot.id,interface.interface,interface.description,interface.ip_netmask,interface.status,vlan.vlan_number AS access FROM network_iot_table AS iot JOIN network_network_table AS network ON network.id = iot.network_id JOIN network_interface_table AS interface ON interface.network_id = network.id LEFT JOIN network_vlan_table AS vlan ON vlan.id = interface.access_id WHERE iot.id = %s"
    # sql_id = "SELECT iot.id AS id FROM network_iot_table AS iot LEFT JOIN network_network_table AS nettable ON iot.network_id = nettable.id LEFT JOIN network_profile_table AS profile ON iot.profile_id = profile.id JOIN network_username_table AS user ON user.id = profile.username_id JOIN network_network_type_table AS network_type ON network_type.id = nettable.network_type_id JOIN network_interface_table AS interface ON interface.network_id = nettable.id JOIN network_group_vlan_table AS group_vlan ON group_vlan.id = profile.group_vlan_id JOIN network_vlan_table AS vlan ON vlan.group_vlan_id = group_vlan.id WHERE iot.id = %s GROUP BY iot.id"
    val_interface = (id,)
    # val_id = (id,)
    interface.execute(sql_interface, val_interface)
    # vlan_id.execute(sql_id, val_id)
    # vlan_id_all = dictfetchall(vlan_id)
    interface_all = dictfetchall(interface)
    data_all = ['configure terminal']
    for interface in interface_all:
        if interface['ip_netmask'] != None and interface['status'] == 1:
            data_all.append('interface'+" "+interface['interface'])
            data_all.append('description'+" "+interface['description'])
            data_all.append('ip address'+" "+interface['ip_netmask'])
            data_all.append('no shutdown')
        elif interface['ip_netmask'] == None and interface['status'] == 0 and interface['access'] == None:
            data_all.append('interface'+" "+interface['interface'])
            data_all.append('shutdown')
        elif interface['ip_netmask'] == None and interface['status'] == 1 and interface['access'] == None:
            data_all.append('interface'+" "+interface['interface'])
            data_all.append('no shutdown')
        elif interface['access'] != None and interface['status'] == 1:
            data_all.append('interface'+" "+interface['interface'])
            if interface['description'] == None:
                data_all.append('switchport mode access')
                data_all.append('switchport access vlan' +
                                " "+interface['access'])
                data_all.append('no shutdown')
            else:
                data_all.append('description'+" "+interface['description'])
                data_all.append('switchport mode access')
                data_all.append('switchport access vlan' +
                                " "+interface['access'])
                data_all.append('no shutdown')
    data_all.append('end')
    data_all.append('wr')
    for tudo in data_all:
        now = datetime.datetime.now()
        list = connection.cursor()
        sql = "insert into network_tudo_table (command,start,iot_id) values (%s,%s,%s)"
        val = (tudo, now, id)
        list.execute(sql, val)
        connection.commit()
    deploy_basic(id)
    return redirect('/')


def on_message_print(client, userdata, message):
    data = message.payload.decode()
    # print(data)
    global mes_error
    if (data.find("% Invalid input detected at '^' marker.")) != -1:
        mes_error = True
        # print(mes_error)
    else:
        mes_error = False
        # print(mes_error)


def deploy_basic(receive):
    cursor2 = connection.cursor()
    sql2 = "SELECT tudo.id AS tudo_id,iot.topic AS topic,iot.id as id,tudo.command AS command FROM network_tudo_table AS tudo JOIN network_iot_table AS iot ON iot.id = tudo.iot_id  WHERE tudo.iot_id = %s AND tudo.end IS NULL"
    where_id = (receive,)
    cursor2.execute(sql2, where_id)
    data2 = dictfetchall(cursor2)
    global mes_error
    for i in data2:
        data_send(i['topic'], i['command'])
        time.sleep(2)
        if mes_error == True:
            now = datetime.datetime.now()
            cursor_edit = connection.cursor()
            sql = "UPDATE network_tudo_table SET end = %s , status = %s WHERE id = %s"
            val = (now, "error", i['tudo_id'])
            cursor_edit.execute(sql, val)
            connection.commit()
            mes_error = None
        elif mes_error == False:
            now = datetime.datetime.now()
            cursor_edit = connection.cursor()
            sql = "UPDATE network_tudo_table SET end = %s , status = %s WHERE id = %s"
            val = (now, "success", i['tudo_id'])
            cursor_edit.execute(sql, val)
            connection.commit()
            # print(now, "UPDATE")
            mes_error = None
    check = connection.cursor()
    sql_check = "SELECT tudo.id AS tudo_id,iot.topic AS topic,iot.id as id,tudo.command AS command,tudo.status AS status,tudo.end AS end  FROM network_tudo_table AS tudo JOIN network_iot_table AS iot ON iot.id = tudo.iot_id  WHERE tudo.iot_id = %s AND tudo.end IS NULL"
    id = (receive,)
    check.execute(sql_check, id)
    data_check = dictfetchall(check)
    for data in data_check:
        if data['end'] == None and data['status'] == None:
            now = datetime.datetime.now()
            edit = connection.cursor()
            sql_edit = "UPDATE network_tudo_table SET end = %s , status = %s WHERE id = %s"
            val_edit = (now, "success", data['tudo_id'])
            edit.execute(sql_edit, val_edit)
            connection.commit()


def data_send(topic, msg):
    mqtt_pub.single(topic, msg, qos=0, hostname="172.16.20.12",
                    port=1883, auth=mqtt_auth)


# Subscribe
client = mqtt.Client()
client.username_pw_set("administrator", "P@ssw0rd@DevNet")
client.connect(hostname, port)
client.subscribe("/30:AE:A4:03:3C:CC/IOT", qos=1)
client.message_callback_add("/30:AE:A4:03:3C:CC/IOT", on_message_print)
