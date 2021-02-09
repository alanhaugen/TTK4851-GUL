# TTK4851-GUL

Bruk av maskinsyn til å detektere og telle mennesker på autofergen

Data folder (data) er på Dropbox. Lag en symbolsk lenke til Dropbox-mappen her, i denne mappen.

> ln -s ~/Dropbox/data data

På Windows, start cmd.exe som admin:

> mklink /D data ..\Dropbox\data

Mer info: https://www.howtogeek.com/howto/16226/complete-guide-to-symbolic-links-symlinks-on-windows-or-linux/

Installer opencv for python:

> pip install opencv-python

Test inference_yolo.py

> ./inference_yolo.py
