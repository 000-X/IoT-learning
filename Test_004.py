import time
from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT
from counterfit_shims_grove.grove_led import GroveLed


CounterFitConnection.init("localhost", 4321)

led = GroveLed(1)
sensor = DHT("11",5)
while True:
    humi, temp = sensor.read();
    print("humidity-> ",humi);
    print("Temperature-> ",temp);
    if humi < 20 and temp > 30:
        print("humidity and Temperature is error!\n")
        led.on();
    else :
        led.off();
    time.sleep(1)
    

