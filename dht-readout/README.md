# DHT readout scripts

Based on adafruit circuitpython dht library

# Requirements
I2C & SPI must be actived in raspi-config:
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

## Packages
```
sudo apt-get install libgpiod2
```

## Virtualenv
```
pip3 install virtualenv

virtualenv venv
. venv/bin/activate
pip3 install -r requirements.txt
```

# Config
DHT should be configured on pin 4 (and pin 17 for the dual readout script)
