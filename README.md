# SAUVC 2022 Repository by Zahid and Ifrah


## For Qualification task

* Navigate into the AUV_2022 -> Tasks -> qualification.py
## For Task 1

* Navigate into the AUV_2022 -> Vision_2022 -> perception and follow the readme inside the 'perception' folder


## Installing OpenCV in Raspberry Pi

* Check if you're using all of your system memory with:
``` df -h ```
* If you're not using most of it, then run: 
``` sudo raspi-config ```
 go to advanced -> expand filesystem -> reboot your pi

* Open terminal and type: 
``` sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev ```

* If you're using a PiCamera run:
``` pip install "picamera[array]" ```
* Users of PiCamera may also have to enable Camera Support:
 ``` sudo raspi-config ```
 Inferface Options -> Legacy Camera Support -> Enable

* Install OpenCV
``` pip install opencv-contrib-python ```
