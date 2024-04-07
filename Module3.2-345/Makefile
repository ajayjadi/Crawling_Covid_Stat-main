# Makefile
COUNTRY_NAME := $(shell read -p "Enter country name: " COUNTRY_NAME; echo $$COUNTRY_NAME)
START_DATE := $(shell read -p "Enter start date (DD-MM-YYYY): " START_DATE; echo $$START_DATE)
END_DATE := $(shell read -p "Enter end date (DD-MM-YYYY): " END_DATE; echo $$END_DATE)


query3:
	python3 mapper3.py "$(COUNTRY_NAME)"| python3 reducer3.py

query4:
	python3 mapper4.py "$(COUNTRY_NAME)" | python3 reducer4.py "$(START_DATE)" "$(END_DATE)"

query5:
	python3 mapper5.py "$(START_DATE)" "$(END_DATE)" | python3 reducer5.py "$(COUNTRY_NAME)" 


