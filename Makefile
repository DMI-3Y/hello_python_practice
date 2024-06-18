# Makefile
run:
	docker-compose up --build

clean:
	docker-compose down -v
	docker system prune -f

.PHONY: run clean
