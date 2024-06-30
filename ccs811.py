
import time
import busio
import board
from board import SCL, SDA
import adafruit_ccs811
# import adafruit_dht
# import matplotlib.pyplot as plt 

i2c = busio.I2C(SCL, SDA)
ccs =  adafruit_ccs811.CCS811(i2c)
# dhtDevice = adafruit_dht.DHT11(board.D4)


while True:
    try:
        # Print the values to the serial port
        print(
            "CO2: {} PPM     TVOC: {} PPM ".format(
                ccs.eco2, ccs.tvoc
            )
        )
        time.sleep(0.5)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        
        continue
    except Exception as error:
        # dhtDevice.exit()
        raise error


