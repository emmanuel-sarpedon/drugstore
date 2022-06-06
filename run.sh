#!/bin/bash
if [ ! -f .env ]
then
  export "$(cat .env)"
else
  export FLASK_APP=app.py
fi


flask run
