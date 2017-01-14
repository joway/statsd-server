pip install -r requirements.txt
cp prov_settings.py local_settings.py
sudo echo "nohup python `pwd`/main.py &" > /etc/init.d/run_statsd.sh
sudo chmod +x /etc/init.d/run_statsd.sh
sudo update-rc.d run_statsd.sh defaults 90
