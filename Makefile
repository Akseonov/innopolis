# Управление docker-compose в разных режимах.
# Запуск: make <цель>, например `make up` или `make script`.

COMPOSE ?= docker compose
SERVICE ?= python
SCRIPT  ?= src/init.py

.DEFAULT_GOAL := help
.PHONY: help up up-d down stop restart logs ps shell python script exec pull clean

help: ## Показать список доступных целей
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

up: ## Запустить в foreground (логи в терминале, Ctrl+C — остановка)
	$(COMPOSE) up

up-d: ## Запустить в фоне (detached)
	$(COMPOSE) up -d

down: ## Остановить и удалить контейнеры и сеть
	$(COMPOSE) down

stop: ## Остановить контейнеры, не удаляя их
	$(COMPOSE) stop

restart: ## Перезапустить сервисы
	$(COMPOSE) restart

logs: ## Смотреть логи в реальном времени
	$(COMPOSE) logs -f $(SERVICE)

ps: ## Показать статус сервисов
	$(COMPOSE) ps

shell: ## Открыть sh внутри работающего контейнера
	$(COMPOSE) exec $(SERVICE) sh

python: ## Открыть интерактивный Python REPL в одноразовом контейнере
	$(COMPOSE) run --rm $(SERVICE) python

script: ## Разовый запуск скрипта: make script SCRIPT=src/init.py
	$(COMPOSE) run --rm $(SERVICE) python $(SCRIPT)

exec: ## Разовая команда в одноразовом контейнере: make exec CMD="pip list"
	$(COMPOSE) run --rm $(SERVICE) $(CMD)

pull: ## Обновить образы
	$(COMPOSE) pull

clean: ## Остановить всё и удалить тома
	$(COMPOSE) down -v --remove-orphans
