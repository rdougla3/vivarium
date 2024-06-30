
import time
import busio
import board
from board import SCL, SDA
import adafruit_ccs811
import adafruit_dht
import matplotlib.pyplot as plt 

# i2c = busio.I2C(SCL, SDA)
# ccs =  adafruit_ccs811.CCS811(i2c)
dhtDevice = adafruit_dht.DHT11(board.D4)


while True:
    try:
        # Print the values to the serial port
        temperature_c = (dhtDevice.temperature if dhtDevice.temperature != None else 0)
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            # "Temp: {:.1f} F / {:.1f} C    Humidity: {}%     CO2: {} PPM     TVOC: {} PPM ".format(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        time.sleep(0.5)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

