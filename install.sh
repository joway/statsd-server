pip install -r requirements.txt
sudo echo "nohup python `pwd`/main.py &" > /etc/init.d/run_statsd.sh
sudo chmod +x /etc/init.d/run_statsd.sh
sudo update-rc.d run_statsd.sh defaults 90
./run.sh
