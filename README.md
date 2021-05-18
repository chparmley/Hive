# FSDI_Final
A django app that counts movement through an area, records it, and displays it in real time.


Installation
------------
clone repo

cd inside cloned folder

*python3 -m venv venv

*source venv/bin/activate

*pip install cmake

*pip install -r requirements.txt


-
what here
How to run
--------------
cd Traffic_Monitor

python3 manage.py runserver 0.0.0.0:8000
-

-
Accessing the app
------------------
On any device on same network as the host:

http://'your.host.ip.address':8000

Register an account then login
-

-
Launching Image Recognition
---------------------------
Leave the app server running and in new terminal withing cloned folder 'FSDI_Final':

cd People-Counting-in-Real-Time

python Run.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel
