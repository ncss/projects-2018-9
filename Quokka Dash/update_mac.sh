#!/bin/bash
cp quokka.py /Volumes/PYBFLASH/
cp boot.py /Volumes/PYBFLASH/
mkdir -p /Volumes/PYBFLASH/drivers
cp drivers/*.py /Volumes/PYBFLASH/drivers
cp demos/${1}.py /Volumes/PYBFLASH/main.py
sync
#screen /dev/tty.usbmodem1412 115200
