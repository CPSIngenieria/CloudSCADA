#!/bin/sh

su - scada
cd /home/scada/webapp/CloudSCADA
git pull origin master

echo "Pull automatico del repositorio central..."
