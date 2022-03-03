#!/bin/bash
echo "установка Python 3.10..."
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.10 python3.10-distutils
echo "установка Nginx"
sudo apt install -y nginx
echo "установка пакетов для работы с принтером"
sudo apt install -y cups hplip unoconv
echo "установка пакетов для работы с сетью"
sudo apt install -y traceroute
echo "установка пакетов для работы сервера"
sudo apt install -y vim tmux
echo "установка Git"
sudo apt install  -y git
echo "установка Python pip"
sudo apt install -y python3-pip
echo "установка poetry"
sudo pip3 install poetry
echo "настройка виртуального окружения poetry"
poetry config virtualenvs.in-project true
echo "установка NodeJS 16.x"
url=https://deb.nodesource.com/setup_16.x 
curl -sL {{url}} -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install -y nodejs
sudo remove nodesource_setup.sh
echo 'готово!'
python3.10 --version
git --version
poetry --version
node -v
npm -v
