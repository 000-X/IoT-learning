import time  
from counterfit_connection import CounterFitConnection  
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor  

CounterFitConnection.init('localhost', 4321)

# 获取光照系数
light_sensor = GroveLightSensor(0)  

while True:  
    light = light_sensor.light   
    print('Light level:', light)  
    time.sleep(1)