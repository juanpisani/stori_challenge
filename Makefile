csv-file ?= example.csv
email-address ?= default@email.com


run:
	docker-compose up -d

process-csv:
	docker-compose run app python manage.py process-csv --csv-file=$(csv-file) --email-address=$(email-address)

stop:
	docker-compose stop
