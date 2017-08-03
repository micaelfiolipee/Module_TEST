RPiHY28bShield
==============
> Raspberrypi 2.8" TFT-LCD Shield : HY28a , HY28b Auto install Script on Raspbian Whezzy

`pi@openmake ~ $ git clone https://github.com/rasplay/RPiHY28bShield`

`pi@openmake ~ $ cd RPiHY28bShield`

[example]

`pi@openmake ~/RPiHY28bShield $ sh setup.sh hy28b`


[included setup.sh]

hy28a.sh : HY28A Model Setup File

hy28b.sh : HY28B Model Setup File

> Raspberrypi 2.8" TFT-LCD Shield : HY28a , HY28b Auto install Script on Raspbian Jessie

$ sudo nano /boot/cmdline.txt

**original**

```
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait
```

**change**

```
dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait fbcon=map:10
```

$ sudo nano /boot/config.txt

 end of add line

```
#same resolution for cdmi and txt
hdmi_force_hotplug=1
hdmi_cvt=320 240 60 1 0 0 0
hdmi_group=2
hdmi_mode=1
hdmi_mode=87
dtparam=spi=on
dtoverlay=hy28b,rotate=90
gpu_mem=256
dtparam=i2c_arm=on
```

`$ con2fbmap 1 1`

`$ sudo reboot`

#### **RaspberryPi Model 3B**

![0_1466169300722_KakaoTalk_Photo_2016-06-17-22-13-53_76.jpeg](https://i.imgur.com/H1EFU2C.jpg) 
