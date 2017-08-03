#! /bin/bash

#Parameters
refreshInterval=1 #Refresh interval in seconds

run_cmd="sh /home/pi/TFTSheildButton/auto_wireless_rasplay.sh"

echo "Run TFT-LCD Button Script."

gpio mode 3 in
gpio mode 2 in

#Main loop
while (true); do
  val1=`gpio read 3`
  val2=`gpio read 2`

  if [ $val1 -eq 0 ] && [ $val2 -ne 0 ]; then
      echo "Press Button 1, so run"
      echo $run_cmd
      $run_cmd
  fi

  if [ $val1 -ne 0 ] && [ $val2 -eq 0 ]; then
      echo "Press Button 2, so run date"
      date
  fi

  if [ $val1 -eq 0 ] && [ $val2 -eq 0 ]; then
      echo "Press Button1, Button 2, so poweroff"
      sudo poweroff
  fi

  sleep $refreshInterval
done
