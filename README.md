# TTK4851-GUL

## Seanet

![alt text](logo.jpg "Captain")

## Plassering av kameraer og bruk av maskinsyn for telling av passasjerer på autofergen

### Setup

Last ned data fra Dropbox: https://www.dropbox.com/sh/hncib87grdepkjy/AAA_whM7rUItDJQAB_48XJq7a?dl=0

Sett data mappen her, i denne mappen.

> cd TTK4851-GUL && unzip ~/Downloads/data.zip

Installer opencv for python:

> pip3 install opencv-python

### Test

Test object_detection_yolov3.py

> python3 object_detection_yolov3.py

### Rapport

Prosess: https://www.overleaf.com/8761576379qgqdtqkyvccb

Prosjekt: https://www.overleaf.com/5628621316bwjsxvqghhgm

### Drive

Google drive: https://drive.google.com/drive/folders/1bFk8L2pCcWhR-ryazxeB5YyInMbRKmNv

### Reklamefilm av autoferjen

Her er hvordan den neste autoferjen vil se ut: https://youtu.be/FuWedx0oLX4?t=107

## For en delt Dropbox-mappe:

Lag en symbolsk lenke til Dropbox-mappen her, i denne mappen.

> ln -s ~/Dropbox/data data

På Windows, start cmd.exe som admin:

> mklink /D data ..\Dropbox\data

Mer info: https://www.howtogeek.com/howto/16226/complete-guide-to-symbolic-links-symlinks-on-windows-or-linux/
