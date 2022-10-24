RUN=docker-compose run --rm project

all:
	DOCKER_BUILDKIT=0 docker-compose build

run:
	docker-compose run --service-ports --rm project

run-all:
	docker-compose up project

shell:
	docker-compose run --rm project /bin/bash

test:
	$(RUN) pytest -x -vvv --pdb

report:
	$(RUN) pytest --cov=apps/ -x --pdb

report-html:
	$(RUN) pytest --cov-report html --cov=apps/ -x --pdb

sort:
	$(RUN) isort --recursive apps project

check-sort:
	$(RUN) isort --recursive --diff apps project

stop:
	docker-compose down

dumpdata:
	$(RUN) python3 manage.py dumpdata --natural-foreign --exclude contenttypes --exclude auth.permission --exclude admin.logentry --exclude sessions.session --indent 4 > fixture.json

migrate:
	$(RUN) python3 manage.py migrate

messages:
	$(RUN) python3 manage.py makemessages -l de -l ar -l fr

compilemessages:
	$(RUN) python3 manage.py compilemessages -l de -l ar -l fr