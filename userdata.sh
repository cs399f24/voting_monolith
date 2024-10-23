#!/bin/bash
yum install -y git
git clone https://github.com/cs399f24/voting_monolith.git
cd voting_monolith
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
yum install -y redis6
systemctl enable redis6
systemctl start redis6
echo "REDIS_HOST=localhost" >> .env
echo "REDIS_PORT=6379" >> .env
cp voting.service /etc/systemd/system
systemctl enable voting
systemctl start voting
