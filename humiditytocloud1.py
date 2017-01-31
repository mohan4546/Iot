import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import mosquitto ,os , urlparse
import mosquitto
client = mosquitto.Mosquitto()

sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
 
GPIO.setmode(GPIO.BOARD)
 
# Defines the GPIO connected to the sensor data pin
pino_sensor=25


# Define event callbacks
def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic + "" + str(msg.qos) + "" + str(msg.payload))

def on_publish(mosq, obj, mid):
    print("")

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mosquitto.Mosquitto()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

# Uncomment to enable debug messages
#mqttc.on_log = on_log

# Parse CLOUDMQTT_URL (or fallback to localhost)
cloudurl = raw_input("enter url of broker:")
url_str = os.environ.get('CLOUDMQTT_URL',cloudurl)
url = urlparse.urlparse(url_str)

# Connect
mqttc.username_pw_set('rhmobvzr','kUNFt2x3YSTv')
mqttc.connect('m11.cloudmqtt.com', 13665)

# Start subscribe, with QoS level 0
mqttc.subscribe("iot", 0)

# Publish a message
#topicname=raw_input("enter topic name:")
#message=raw_input("message:")


# Continue the network loop, exit when an error occurs
rc = 0

while(1):
   # Read the sensor
   umid, temp = Adafruit_DHT.read_retry (sensor, pino_sensor);
   # If reading case is ok, it shows the values ​​on the screen
   if umid is not None and temp is not None:
     print ("Temperature = {0: 0.1f} Humidity = {1: 0.1f} \ n"). format (temp, umid);
     print ("Wait 5 seconds to re-read ... \ n");
     mqttc.publish("temperature",temp)
     mqttc.publish("humidity",umid)
     time.sleep (10)
   else:
     # Communication error message with the sensor
     print ("Failed to read data from DHT11 !!!")


while rc == 0:
    rc = mqttc.loop()
print("rc: " + str(rc))
     
     
