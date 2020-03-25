import time
import board
import adafruit_dht
 
# Initial the dht device, with data pin connected to:
dhtDevice1 = adafruit_dht.DHT11(board.D4)
dhtDevice2 = adafruit_dht.DHT22(board.D17)

while True:
    try:
        # Print the values to the serial port
        print(
            "Sensor 1: Temp: {:.1f} C    Humidity: {}% ".format(
                dhtDevice1.temperature, dhtDevice1.humidity
            )
        )
        print(
            "Sensor 2: Temp: {:.1f} C    Humidity: {}% ".format(
                dhtDevice2.temperature, dhtDevice2.humidity
            )
        )
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
 
    time.sleep(4.0)
