import sys

for line in sys.stdin:
    # Strip the line of any leading/trailing whitespace
    line = line.strip().replace('$', '')
    
    # Check if the line is not empty
    if line:
        parts = line.split()
        # Check if there are at least two parts
        if len(parts) >= 2:
            country_name = parts[0]
            numbers = '-'.join(parts[1:])
            new_string = f"{country_name}-{numbers}"
            print(new_string)
        else:
            print("Invalid input format:", line)