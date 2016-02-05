PyBankId-Proxy
========

PyBankID-Proxy is a proxy to perform BankID auth requests.

For more details about BankID implementation, see the [official documentation](https://www.bankid.com/bankid-i-dina-tjanster/rp-info).

Installation
------------
PyBankId-Proxy can be installed the following way:

```bash
git clone https://github.com/magandrez/pybankid-proxy

virtualenv -p /usr/local/bin/python env

source env/bin/activate

pip install -r requirements.txt

python run.py
```

This proxy is built to be run in Heroku. Given the [Heroku Toolbelt](https://toolbelt.heroku.com/) is already installed:

```bash

heroku create

heroku apps:rename myproxy

git push heroku master   
```

And test it in the browser https://myproxy.herokuapp.com

To see Heroku logs:

```bash
heroku logs -t
```

Requirements
------------

- Python >= 2.7.9
- Virtualenv >= 1.11.6

### Included in `requirements.txt`
- Flask >= 0.10.1
- gunicorn >= 19.3.0
- Jinja2 >= 2.8
- MarkupSafe >= 0.23
- Werkzeug >= 0.11.3
- itsdangerous >= 0.24
- wsgiref >= 0.1.2
