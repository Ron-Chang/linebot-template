MAKEFLAGS += --silent

# ----- config ----- #

ENV_FILE=.env
CONFIRM=confirm

# -- dependencies -- #

include mkfile/Makefile.function
include mkfile/Makefile.style
include $(ENV_FILE)

# ----- Basic ----- #

build:  ## Build App
	@export ACTION="BUILD     " APP="$(APP_NAME).app" && make .cmd-info
	@docker compose --env-file $(ENV_FILE) build

up:  ## Up App
	@export ACTION="UP        " APP="$(APP_NAME).app" && make .cmd-info
	@docker compose --env-file $(ENV_FILE) up -d app

down:  ## Down App
	@export ACTION="DOWN      " APP="$(APP_NAME).app" && make .cmd-info
	@docker compose --env-file $(ENV_FILE) rm -sf app

run:  ## Execute App with $bash
	@clear
	@export ACTION="EXECUTE   " APP="$(APP_NAME).app" && make .cmd-info
	@docker exec -it "$(APP_NAME)" bash

# ----- Advanced ----- #

launch: up-redis  ## Launch Services
	@export ACTION="LAUNCHED  " APP="services" && make .cmd-info

close: down-redis  ## Close Services
	@export ACTION="CLOSED    " APP="services" && make .cmd-info

re: down up  ## Recreate App
	@export ACTION="RECREATED " APP="$(APP_NAME).app" && make .cmd-info

uu: launch up  ## Launch Services & Up App

dd: down close  ## Down App & Close Services

restart: dd uu  ## Restart Services & App
	@export ACTION="RESTARTED " APP="services & app" && make .cmd-info

uur: uu run  ## Launch Services & Up App & Execute App

rr: re run  ## Restart App & Execute App

# ----- Optional ----- #

up-redis:  ## Up redis
	@export ACTION="UP        " APP="$(APP_NAME).redis" && make .cmd-info
	@docker compose --env-file $(ENV_FILE) up -d redis

down-redis:  ## Down redis
	@export ACTION="DOWN      " APP="$(APP_NAME).redis" && make .cmd-info
	@docker compose --env-file $(ENV_FILE) rm -sf redis
