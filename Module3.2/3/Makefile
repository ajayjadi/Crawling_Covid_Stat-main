COUNTRY_NAME := $(shell read -p "Enter COUNTRY_NAME: " COUNTRY_NAME; echo $$COUNTRY_NAME)



all: mapper 


# Target to run mapper.py for each file and then execute reducer.py
mapper:
	@for year_folder in ../../Module2/$(COUNTRY_NAME)*.txt; do \
        python3 mapper.py "$$year_folder" & \
    wait;\
    done; \
    
