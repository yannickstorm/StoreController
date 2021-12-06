#!/bin/sh

echo "cd to the folder"

cd ~/Documents/StoreController/StoreController/StoreBackEnd/

echo "activate the virtual env"
source ~/Documents/StoreController/StoreController/StoreBackEnd/env/bin/activate

echo "start app"
sudo nohup python3 app.py &

echo "connect to http://storecontrolstation:5000/store/"

