# TTK4851-GUL

## Bruk av maskinsyn til å detektere og telle mennesker på autofergen

### Setup

Last ned data fra Dropbox: https://www.dropbox.com/sh/35sw2e2k2mnfpey/AABfc_XbsDZG3jrlAkSZ40I8a?dl=0

Sett data mappen her, i denne mappen.

> cd TTK4851-GUL
> unzip ~/Downloads/data.zip

Installer opencv for python:

> pip3 install opencv-python

### Test

Test object_detection_yolo.py

> python3 object_detection_yolo.py

### Rapport

Prosess: https://www.overleaf.com/4512238873cndkktsqvgwm 

Prosjekt: https://www.overleaf.com/1614163417dvgfpsqhwcvq 

### Reklamefilm av autoferjen

Her er hvordan den neste autoferjen vil se ut: https://youtu.be/FuWedx0oLX4?t=107

## For en delt Dropbox-mappe:

Lag en symbolsk lenke til Dropbox-mappen her, i denne mappen.

> ln -s ~/Dropbox/data data

På Windows, start cmd.exe som admin:

> mklink /D data ..\Dropbox\data

Mer info: https://www.howtogeek.com/howto/16226/complete-guide-to-symbolic-links-symlinks-on-windows-or-linux/
