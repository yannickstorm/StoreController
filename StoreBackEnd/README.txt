192.168.43.158

ssh pi@storecontrolstation

cd Documents/StoreController/StoreController/StoreBackEnd/
source env/bin/activate
sudo nohup python3 app.py &

http://storecontrolstation:5000/store/






------------------------------------ StartStoreController.sh script ---------------------------------
# Copy from mac to the pi
scp StartStoreController.sh pi@StoreControlStation:~/
# Copy to bin folder for sh files
sudo cp StartStoreController.sh /usr/local/bin/
# give run permission to the script
sudo chmod +x /usr/local/bin/StartStoreController.sh

Then the Store controller can be started by running StartStoreController.sh
Limitations: the sourcing of the virtual env does not work this way for the moment!!











