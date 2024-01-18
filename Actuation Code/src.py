import random
import time
from paho.mqtt import client as mqtt_client
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
# IP and Port details
broker = '192.168.43.151'
port = 1883
topic = "sensor/temperature"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'

threshold_value = 27
flag = 0
flag1 = 1
# def send_sms():
#     print("in")
#     curl_command = '''
#         curl -X POST \
#         -H "Authorization: Bearer 654e30fcc67a4e889a869b1b5c9aee1a" \
#         -H "Content-Type: application/json" -d '
#         {
#             "from": "447520651011",
#             "to": [ "917998850274" ],
#             "body": "ALERT! High Temperature Detected."
#         }' \
#         "https://sms.api.sinch.com/xms/v1/a22cbcb488ae42d3b797fcc5020b2620/batches"
#     '''

#     response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

#     print(response.stdout)
#     print(response.stderr)
# def send_sms():
#     print("in")
#     curl_command = '''

#         curl -X POST \
#         -H "Authorization: Bearer 508b1cb2168f48fc8f4bb8be1cf11b87" \
#         -H "Content-Type: application/json" -d '
#         {
#             "from": "447520652859",
#             "to": [ "918697421053" ],
#             "body": "ALERT! High Temperature Detected."
#         }' \
#         "https://sms.api.sinch.com/xms/v1/383f62034bc44b979212cc7fb4c3d1a8/batches"

#     '''

#     response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

#     print(response.stdout)
#     print(response.stderr)

def send_smsr():
    curl_command = '''

        curl -X POST \
        -H "Authorization: Bearer 98eccdc87033440eabede2dcb4724fef" \
        -H "Content-Type: application/json" -d '
        {
            "from": "447520652479",
            "to": [ "919748346608" ],
            "body": "ALERT! High Temperature Detected.Cooling System initiated."
        }' \
        "https://sms.api.sinch.com/xms/v1/b890490d1ceb4fff904851f7b74267c1/batches"

    '''
    response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    print(response.stdout)
    print(response.stderr)

def send_smsg():
    curl_command = '''

        curl -X POST \
        -H "Authorization: Bearer 98eccdc87033440eabede2dcb4724fef" \
        -H "Content-Type: application/json" -d '
        {
            "from": "447520652479",
            "to": [ "919748346608" ],
            "body": "Temperature Undercontrol."
        }' \
        "https://sms.api.sinch.com/xms/v1/b890490d1ceb4fff904851f7b74267c1/batches"

    '''
    response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    print(response.stdout)
    print(response.stderr)


# Connect to mqtt broker
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!!!Waiting for Data....")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# subscribe to mqtt topic
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global flag, flag1
        payload_value = float(msg.payload.decode())

        if payload_value > threshold_value:
            print("Red LED")
            GPIO.output(17, GPIO.HIGH)

            # Send SMS when threshold is exceeded
            if flag == 0:
                flag = 1
                flag1 = 0
                send_smsr()
        else:
            flag = 0
            print("Green LED on")
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.HIGH)
            time.sleep(1)
            if flag1 == 0:
                flag1 = 1
                flag = 0
                send_smsg()
            print("Green LED off")
            GPIO.output(27, GPIO.LOW)

    client.subscribe(topic)
    client.on_message = on_message

# infinite loop
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()










