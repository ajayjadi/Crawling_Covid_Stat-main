# Define variables for start and end dates
START_DATE := $(shell read -p "Enter start date (DD-MM-YYYY): " START_DATE; echo $$START_DATE)
END_DATE := $(shell read -p "Enter end date (DD-MM-YYYY): " END_DATE; echo $$END_DATE)

# Define targets
.PHONY: all mapper reducer clean

all: mapper1  reducer


# Target to run mapper.py for each file and then execute reducer.py
mapper:
	@for year_folder in ../../Module2/20*/*.txt; do \
        python3 mapper.py "$$year_folder" "$$year_folder" & \
    done; \
    wait | python3 reducer.py "$(START_DATE)" "$(END_DATE)" > result.txt

# Target to clean up temporary files
clean:
	@echo "Cleaning up temporary files..."
	@rm -f result.txt

mapper1:
	@{ \
        for year_folder in ../../Module2/20*/*.txt; do \
            python3 mapper.py "$$year_folder" "$$year_folder"; \
        done; \
        wait; \
    } > temp.txt

	
reducer:
	cat temp.txt | python3 reducer.py "$(START_DATE)" "$(END_DATE)" > result.txt