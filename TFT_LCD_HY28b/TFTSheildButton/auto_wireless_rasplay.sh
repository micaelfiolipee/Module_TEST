echo "mount from /dev/sda2 to /mnt/usb1"
sudo mkdir /mnt/usb1
sudo mount /dev/sda2 /mnt/usb1

echo "sudo cp /mnt/usb1/etc/network/interfaces /mnt/usb1/etc/network/interfaces.bak"
sudo cp /mnt/usb1/etc/network/interfaces /mnt/usb1/etc/network/interfaces.bak
echo "/mnt/usb1/etc/network/interfaces change"
sudo sed -i '/wlan0/d' /mnt/usb1/etc/network/interfaces
sudo sed -i '/iface default inet dhcp/d' /mnt/usb1/etc/network/interfaces


sudo sed -i '$a\allow-hotplug wlan0' /mnt/usb1/etc/network/interfaces
sudo sed -i '$a\iface wlan0 inet dhcp' /mnt/usb1/etc/network/interfaces
sudo sed -i '$a\wireless-essid rasplay' /mnt/usb1/etc/network/interfaces
sudo sed -i '$a\wireless-mode managed' /mnt/usb1/etc/network/interfaces
sudo sed -i '$a\iface default inet dhcp' /mnt/usb1/etc/network/interfaces

echo "unmount /mnt/usb1"
sudo umount /mnt/usb1

echo "now, remove usb, and using sd to another Rpi"
