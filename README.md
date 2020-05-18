# rpi_cooler_python
This is a simple python script that takes care of active cooling of my Raspberry Pi
It is set up as a systemd service that is run on boot

### features:
it creates a textfile that shows the current CPU temperature. The file is updated with every iteration of the program

it checks for a file named 'on' in its directory. If the file exists, the cooler runs regardless of the CPU temperature. This is for manual toggle of the cooler

### important note about disk IO:
this script writes about 4KB worth of data on disk in each iteration. In the current configuration where it iterates every 5 seconds, it writes about 1/2GB per month. This contributes to gradual wearing down of the drive. Therefore, you may want to change the location of the fan_state file to a RAM-based location, e.g. /tmp.
