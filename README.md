## Description
CCS project

## Prerequisites

You should have `python`, `python-virtualenv`, `python-pip`, `postgresql` and `git`
Install [wkhtmltopdf](https://wkhtmltopdf.org/)

## Installation

### Postgres

```
$ sudo su postgres -c psql

postgres$ create user <user> with password '<password>';

postgres$ create database <database> owner <user> encoding 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';
```

#### Only for local purposes to use fabric

```sh
postgres$ alter user <user> with superuser;
```

Edit the `/etc/postgresql/13.x/main/pg_hba.conf` file as root user:

```
local all postgres trust

local all all trust
```

Restart the service

```sh
/etc/init.d/postgresql restart
```


## Configure the project

### Run project

Initially (only first time) run:

```sh
$ python3 -m venv ccs_env
$ source bin/activate
(ccs_env) $ pip install -r requirements.txt
(ccs_env) $ ./manage.py check
(ccs_env) $ ./manage.py migrate
```

Everytime:
```sh
$ ./server.sh
```
