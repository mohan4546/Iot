Import Adafruit_DHT
Import RPi.GPIO as GPIO
Import time
 
# Defines sensor type
Sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
 
GPIO.setmode (GPIO.BOARD)
 
# Defines the GPIO connected to the sensor data pin
Pino_sensor = 25
 
# Initial information
Print ("*** reading the values ​​of temperature and humidity");
 
While (1):
   # Read the sensor
   Umid, temp = Adafruit_DHT.read_retry (sensor, pin_sensor);
   # If reading case is ok, it shows the values ​​on the screen
   If umid is not None and temp is not None:
     Print ("Temperature = {0: 0.1f} Humidity = {1: 0.1f} \ n"). Format (temp, umid);
     Print ("Wait 5 seconds to re-read ... \ n");
     Time.sleep (5)
   Else:
     # Communication error message with the sensor
     Print ("Failed to read data from DHT11 !!!")
