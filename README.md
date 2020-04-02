# rpi_cooler_python
This is a simple python script that takes care of active cooling of my Raspberry Pi
It is set up as a systemd service that is run on boot

### features:
it creates a textfile that shows the current CPU temperature. The file is updated with every iteration of the program

it checks for a file named 'on' in its directory. If the file exists, the cooler runs regardless of the CPU temperature. This is for manual toggle of the cooler
