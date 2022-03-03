import paho.mqtt.client as mqtt
import re
from django.db import connection


hostname = "172.16.20.12"
port = 1883


def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def on_message_print(client, userdata, message):
    mes = message.payload.decode()
    # print(mes)
    # data_clean = re.search('5 minute output rate(.*)', mes)
    # if data_clean != None:
    #     data_clean = data_clean.group()
    #     print(data_clean)
    #     data_clean = data_clean.split()
    #     data_interface = re.search('show interfaces(.*)', mes)
    #     data_interface = data_interface.group()
    #     print(data_interface)
    #     data_interface = data_interface.split()
    #     insert = connection.cursor()
    #     sql_insert = "insert into network_traffic_table (topic,interface,packets) values (%s,%s,%s)"
    #     val_insert = (
    #         "/30:AE:A4:03:3C:CC/DevNet/String_Serial/Sub", data_interface[2], data_clean[6])
    #     insert.execute(sql_insert, val_insert)
    #     connection.commit()
    # else:
    #     pass

    # print(data_clean[6])


# Subscribe
client = mqtt.Client()
client.username_pw_set("administrator", "P@ssw0rd@DevNet")
client.connect(hostname, port)
client.subscribe("/30:AE:A4:03:3C:CC/DevNet/String_Serial/Pub", qos=1)
client.message_callback_add(
    "/30:AE:A4:03:3C:CC/DevNet/String_Serial/Pub", on_message_print)
