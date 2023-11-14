## Schema Service

REST Service to learn about json schema validation in python with cerberus, pyjq and pytest

## Technologies
* [Python 3.10.*](https://www.python.org/)
* [Cerberus](https://docs.python-cerberus.org/)
* [Pytest](https://docs.pytest.org/en/7.4.x/)

## Setup Project
Clone project and run the follow scripts into project root: 

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Run unit tests
```bash
pytest --cov=src/core/domain --cov-report=html
```

The command above will generate htmlcov directory. Open htmlcov/index.html in your favorite browser to access coverage report.

