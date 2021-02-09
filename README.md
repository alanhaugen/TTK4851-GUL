# TTK4851-GUL

## Bruk av maskinsyn til å detektere og telle mennesker på autofergen

### Setup

Last ned data fra Dropbox: https://www.dropbox.com/sh/35sw2e2k2mnfpey/AABfc_XbsDZG3jrlAkSZ40I8a?dl=0

Sett data mappen her, i denne mappen.

> unzip ~/Downloads/data.zip .

Installer opencv for python:

> pip install opencv-python

### Test

Test inference_yolo.py

> ./inference_yolo.py

## For en delt Dropbox-mappe:

Lag en symbolsk lenke til Dropbox-mappen her, i denne mappen.

> ln -s ~/Dropbox/data data

På Windows, start cmd.exe som admin:

> mklink /D data ..\Dropbox\data

Mer info: https://www.howtogeek.com/howto/16226/complete-guide-to-symbolic-links-symlinks-on-windows-or-linux/
