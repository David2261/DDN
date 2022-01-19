run:
	docker run -d -p 80:4200 -v logs:/app/data --env-file ./config/.env --rm --name logsapp logsapp:volumes
stop:
	docker stop logsapp