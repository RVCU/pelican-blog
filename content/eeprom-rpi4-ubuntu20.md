Title: Updating EEPROM on Ubuntu 20.24 RPI4
Date: 2020-10-16
Category: tech
Tags: ubuntu, rpi

rpi foundation recently released support for booting from usb for rpi4 model. I am running Ubuntu 20 on my rpi4s currently which doesn't ship with the regular rpi4 userland which means no firmware update and no configuring to boot from usb unless we hack so we hack.

First thing you need is the userland so we can have the **vcgencmd** that is needed by the eeprom updater

```
{
sudo apt install cmake gcc-aarch64-linux-gnu g++-aarch64-linux-gnu
git clone https://github.com/raspberrypi/userland
cd userland
./buildme --aarch64
}
```
the userland commands are now installed to your system. We're only interested in `vcgencmd` which is in the `/opt/vc/bin/` dir. Because of the weird place the tools are installed they must be added to the LD_LIBRARY_PATH

`LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/vc/lib/ && export LD_LIBRARY_PATH`

created a link to the file in `/usr/sbin/` so the rpi-eeprom tools can find the vcgencmd
`ln -s /opt/vc/bin/vcgencmd /usr/sbin/vcgencmd`

we can now use the eeprom tools to update the eeprom
```
{
git clone https://github.com/raspberrypi/rpi-eeprom.git
cd rpi-eeprom
BOOTFS=/boot/firmware ./rpi-eeprom-update -a
}
```

and edit the current bootconfig 

`BOOTFS=/boot/firmware ./rpi-eeprom-config --edit` 

if the edit command is complaining it can't find the `rpi-eeprom-update` command just edit `rpi-eeprom-config` file with `sed -i 's/rpi-eeprom-update/\.\/rpi-eeprom-update/g' /opt/vc/bin/vcgencmd` since they are in the same dir and trying to move the update tool to a another bin dir had some issues.

This is pretty ugly and there is definitely a cleaner way but I was doing this on the SD card OS I no longer cared about so :) 
