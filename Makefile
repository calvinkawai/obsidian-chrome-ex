#!/bin/zsh
VENV_DIR=.venv

run:
	$(VENV_DIR)/bin/python -m fastapi run backend --reload
