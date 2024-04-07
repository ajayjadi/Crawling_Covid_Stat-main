# Define variables for country name
COUNTRY_NAME := $(shell read -p "Enter country name: " COUNTRY_NAME; echo $$COUNTRY_NAME)

query2:
	@read -p "Enter start date (DD-MM-YYYY): " START_DATE; \
	read -p "Enter end date (DD-MM-YYYY): " END_DATE; \
	python3 mapper2.py "$(COUNTRY_NAME)" "$$START_DATE" "$$END_DATE" | python3 combiner2.py | python3 reducer2.py

query1:
	python3 mapper1.py "$(COUNTRY_NAME)" | python3 reducer1.py
