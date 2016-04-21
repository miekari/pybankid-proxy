PyBankId-Proxy
========

PyBankID-Proxy is a proxy to perform BankID auth requests.

For more details about BankID implementation, see the [official documentation](https://www.bankid.com/bankid-i-dina-tjanster/rp-info).

This proxy uses [Flask](http://flask.pocoo.org/) engine and relies on [pybankid](https://github.com/hbldh/pybankid) wrapper made by Henrik Blidh ([hbldh](https://github.com/hbldh)). This proxy has been designed with Heroku in mind.

PyBankId-Proxy implements Basic Auth using Flask-BasicAuth package. It is recommended to keep all connections between server and client under SSL/TLS (HTTPS).

This code has not been tested with Python3, strange things might occur.

Installation
------------
PyBankId-Proxy can be installed the following way:

```bash
git clone https://github.com/magandrez/pybankid-proxy

virtualenv -p /usr/local/bin/python env

source env/bin/activate

pip install -r requirements.txt

#Set credentials in local env
export PASS="mypassword"
export USR="myuser"

#Run locally
python run.py
```
The service is accessible from localhost:  https://localhost:5000/authenticate/PERSONNUMMER

Where ```PERSONNUMMER``` can be generated randomly using [fejk.se](https://fejk.se/)

This proxy is built to be run in Heroku. Given the [Heroku Toolbelt](https://toolbelt.heroku.com/) is already installed, the deployment can be done the following way:

```bash
heroku apps:create myproxy

heroku config:set PASS="mypassword"

heroku config:set USR="myuser"

git push heroku master

#Heroku logs
heroku logs -t

#Run Heroku locally (results in localhost)
heroku local
```

The service is accessible as a Heroku app:  https://myproxy.herokuapp.com/authenticate/PERSONNUMMER

Recommendations
------------
- Python >= 2.7.9 Is the minimum recommended version due to the new re-implementation of all SSL modules.
- Virtualenv >= 1.11.6 Is recommended for a healthy dev environment.

### Requirements (included in `requirements.txt`)
- Flask 0.10.1
- Flask-BasicAuth 0.2.0
- gunicorn 19.3.0
- Jinja2 2.8
- MarkupSafe 0.23
- Werkzeug 0.11.3
- itsdangerous 0.24
- wsgiref 0.1.2



this has been modified
