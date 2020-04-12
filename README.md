# AWS + Ansible + Flask App Stack

As it says on the tin.


## Prerequisites

1. Vagrant + VirtualBox (if you'd like to run this locally)
2. Python 3.6+

## Setup

```
pip install requirements.txt
```

## Run Flask App Locally

```
cd src/flask-app
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

Open http://127.0.0.1:5000/ - should show "Hello, world!"
