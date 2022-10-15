#!/bin/bash
source my_env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
flask run