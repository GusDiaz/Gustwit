#!/bin/bash
ENVDIRECTORY=".env"
if [ ! -d "$ENVDIRECTORY" ]; then
  virtualenv --python=python2 "$ENVDIRECTORY"
fi

source .env/bin/activate
pip install -r requirements.txt
echo "Gustwit running..."
python app.py
echo "Bye!"
deactivate
