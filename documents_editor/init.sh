#!/bin/bash

ip_addr=$1

if [ -z ${ip_addr} ]; then

    echo "задайте ip для принтера"
    exit 1
else
    echo "установка утилит для работы с сетью"
    apt install -y net-tools iputils-ping

    echo "устанка утилит для работы с принтером"
    apt install -y cups cups-client lpr hplip unoconv

    /etc/init.d/cups start
    hp-setup -i $ip_addr

    echo "список доступных принтеров:"

    printer=`lpstat -p | cut -d \  -f2`
    lpoptions -d $printer

    echo "готово"
    exit 0
fi

# запуск приложения
uvicorn main:app --host 0.0.0.0 --reload --workers 2
