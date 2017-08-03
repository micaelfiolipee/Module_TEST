WebIOPi-0.7.1 Patch for Raspberry B+, Pi2, and Pi3
=============================================

You have full access to all header pins (40 pins) on the Web interface.

![Alt Text](http://cdn-ak.f.st-hatena.com/images/fotolife/h/htana23/20150122/20150122174651.png)

## Usage
------
$ wget http://downloads.sourceforge.net/project/webiopi/WebIOPi-0.7.1.tar.gz  
$ tar xvzf WebIOPi-0.7.1.tar.gz  
$ cd WebIOPi-0.7.1  
$ wget https://github.com/rasplay/WebIOPi-0.7.1-Patch/blob/master/webiopi-pi2bplus.patch  
$ patch -p1 -i webiopi-pi2bplus.patch  
$ sudo ./setup.sh

### How to Start WebIOPi

> Follow the steps below if Raspbian is installed by Jessie  

$ sudo webiopi -d -c /etc/webiopi/config

### Running WebIOPi (Daemon)
> You can also start/stop the background service, the configuration will be loaded from /etc/webiopi/config.

$ sudo /etc/init.d/webiopi start
$ sudo /etc/init.d/webiopi stop

### Auto start at boot
> To setup your system to start webiopi at boot :

$ sudo update-rc.d webiopi defaults

> To remove webiopi start from boot :
$ sudo update-rc.d webiopi remove
