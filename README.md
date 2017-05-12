# Audree server

## First-time setup

Languages/applications needed
- Python 3.5
- Postgres [postgres](https://www.postgresql.org)

The app runs within a virtual environment. To [install virtualenv](https://virtualenv.readthedocs.org/en/latest/installation.html), run
```shell
    [sudo] pip install virtualenv
```

Install virtualenvwrapper
```shell
    [sudo] pip install virtualenvwrapper
```

Create a database for the server
```shell
    [sudo] createdb audree
```

Create a local environment.sh file containing the following:
```shell
echo "
export DJANGO_SETTINGS_MODULE='audree.settings.dev'
export DATABASE_URL='postgres://localhost/audree'
export SECRET_KEY='REPLACE ME WITH AN ACTUAL SECRET KEY'
"> environment.sh
```

Make a virtual environment for this app:
```shell
    mkvirtualenv -p /usr/local/bin/python3.5 audree
```

Install dependencies
```shell
    ./scripts/bootstrap.sh
```

## Running the application

Running with django runserver:
```shell
    workon audree
    python manage.py runserver 0:8000
```
Then visit [localhost:8000](http://localhost:8000)

## Running tests

Tests include a pep8 style check, django test script and coverage report.

```shell
    workon audree
    python run_tests.py
```
