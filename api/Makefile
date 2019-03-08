venv_path ?=.venv
source_venv =. $(venv_path)/bin/activate &&

deps: venv
	$(source_venv) pip install -r requirements.txt

venv:
	test -d $(venv_path) || python3 -m venv $(venv_path)

run: deps
	$(source_venv) FLASK_APP=app.py flask run

debug: deps
	$(source_venv) MONGODB_URL="mongodb://localhost:27017" FLASK_ENV=development FLASK_APP=app.py flask run

clean:
	find . -name \*.pyc -delete; find . -type d -name __pycache__ -delete
